# DemoML
Simple movie recommendation system using a custom dataset to provide personalized movie suggestions based on genre similarity.

# Simple Movie Recommendation System

This project is a simple movie recommendation system built using Flask. It uses a custom dataset to provide personalized movie suggestions based on genre similarity. The system leverages TF-IDF vectorization and cosine similarity to find and recommend movies that are similar to a given movie title.

## Features

- Load and process a custom dataset of movies.
- Use TF-IDF vectorization to convert movie genres into feature vectors.
- Calculate cosine similarity between movies based on their genre vectors.
- Provide movie recommendations through a web interface.

## Setup and Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/DemoML.git
    cd movie-recommendation-system
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Prepare your dataset**:
    - Ensure your dataset (`dataset.csv`) is in the root directory of the project.
    - The dataset should have at least the following columns: `title` and `genre`.

4. **Run the application**:
    ```bash
    python app.py
    ```

5. **Access the web interface**:
    - Open your web browser and go to `http://127.0.0.1:5000/`.

## Code Overview

### Flask Application Setup

The Flask app is initialized and routes are defined for the home page (`'/'`) and the recommendation endpoint (`'/recommend'`).

### Loading Dataset

The dataset is loaded using `pandas.read_csv` and stored in the `data` variable. The dataset is expected to have at least `title` and `genre` columns.

### TF-IDF Vectorization

The `genre` column is used to create a TF-IDF matrix, which transforms the text into feature vectors. The `TfidfVectorizer` from `sklearn` is used for this purpose, with English stop words removed.

### Cosine Similarity Calculation

Cosine similarity is computed between all movies using their TF-IDF vectors, resulting in a similarity matrix (`cosine_sim`).

### Recommendation Function

The `get_recommendations` function takes a movie title and returns a list of 10 most similar movies based on the cosine similarity scores. The function handles case insensitivity by converting titles to lowercase and returns an appropriate message if the title is not found in the dataset.

### Routes

- The root route (`'/'`) serves the `index.html` template, which should contain the UI for entering movie titles and displaying recommendations.
- The `/recommend` route handles POST requests, expecting a JSON payload with a `title` field. It returns the recommendations as a JSON response.
