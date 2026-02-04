import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")

# Create user-movie matrix
user_movie_matrix = ratings.pivot_table(
    index='userId',
    columns='movieId',
    values='rating'
)

# Fill missing ratings with 0
user_movie_matrix = user_movie_matrix.fillna(0)

# Compute similarity between users
user_similarity = cosine_similarity(user_movie_matrix)

user_similarity_df = pd.DataFrame(
    user_similarity,
    index=user_movie_matrix.index,
    columns=user_movie_matrix.index
)

def recommend_movies(user_id, num_recommendations=5):
    # Get similar users (excluding the user himself)
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)[1:]

    # Movies already rated by user
    user_rated_movies = ratings[ratings['userId'] == user_id]['movieId'].tolist()

    recommendations = {}

    for sim_user, similarity_score in similar_users.items():
        sim_user_ratings = ratings[ratings['userId'] == sim_user]

        for _, row in sim_user_ratings.iterrows():
            if row['movieId'] not in user_rated_movies:
                recommendations[row['movieId']] = recommendations.get(
                    row['movieId'], 0
                ) + similarity_score * row['rating']

    # Sort and get top recommendations
    recommended_movie_ids = sorted(
        recommendations,
        key=recommendations.get,
        reverse=True
    )[:num_recommendations]

    return movies[movies['movieId'].isin(recommended_movie_ids)]['title']

# Test
if __name__ == "__main__":
    print(recommend_movies(user_id=1))
