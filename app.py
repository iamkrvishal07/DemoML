from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

app = Flask(__name__)

# Load the dataset
data = pd.read_csv('dataset.csv')

# Process genres for the TF-IDF vectorizer
data['genre'] = data['genre'].fillna('')
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['genre'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to get recommendations based on cosine similarity
def get_recommendations(title, cosine_sim):
    # Convert title to lowercase for case-insensitive comparison
    title = title.lower()
    # Find the index of the movie that matches the title
    idx = data.index[data['title'].str.lower() == title].tolist()
    if not idx:
        return ["Movie title not found in the dataset."]
    idx = idx[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return data['title'].iloc[movie_indices].tolist()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    title = data.get('title')
    recommendations = get_recommendations(title, cosine_sim)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
