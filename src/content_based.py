import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load movie data
movies = pd.read_csv("data/movies.csv")

# Replace | with space in genres
movies['genres'] = movies['genres'].str.replace('|', ' ', regex=False)

# Convert genres into numerical features
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'])

# Compute cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Map movie titles to indices
indices = pd.Series(movies.index, index=movies['title'])

def recommend_movies(movie_title, num_recommendations=5):
    idx = indices[movie_title]
    similarity_scores = list(enumerate(cosine_sim[idx]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    top_movies = similarity_scores[1:num_recommendations + 1]
    movie_indices = [i[0] for i in top_movies]

    return movies['title'].iloc[movie_indices]

# Test the system
if __name__ == "__main__":
    print(recommend_movies("Toy Story (1995)"))
