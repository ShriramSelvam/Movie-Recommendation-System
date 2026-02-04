import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")

# ---------- CONTENT-BASED SETUP ----------
movies['genres'] = movies['genres'].str.replace('|', ' ', regex=False)

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'])
content_similarity = cosine_similarity(tfidf_matrix)

title_to_index = pd.Series(movies.index, index=movies['title'])

def content_based_recommend(movie_title, top_n=10):
    idx = title_to_index[movie_title]
    scores = list(enumerate(content_similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    movie_indices = [i[0] for i in scores[1:top_n+1]]
    return movies.iloc[movie_indices][['movieId', 'title']]

# ---------- COLLABORATIVE FILTERING SETUP ----------
user_movie_matrix = ratings.pivot_table(
    index='userId',
    columns='movieId',
    values='rating'
).fillna(0)

user_similarity = cosine_similarity(user_movie_matrix)
user_similarity_df = pd.DataFrame(
    user_similarity,
    index=user_movie_matrix.index,
    columns=user_movie_matrix.index
)

def collaborative_recommend(user_id, top_n=10):
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)[1:]
    user_movies = ratings[ratings['userId'] == user_id]['movieId'].tolist()

    scores = {}

    for sim_user, sim_score in similar_users.items():
        sim_user_ratings = ratings[ratings['userId'] == sim_user]
        for _, row in sim_user_ratings.iterrows():
            if row['movieId'] not in user_movies:
                scores[row['movieId']] = scores.get(row['movieId'], 0) + sim_score * row['rating']

    movie_ids = sorted(scores, key=scores.get, reverse=True)[:top_n]
    return movies[movies['movieId'].isin(movie_ids)][['movieId', 'title']]

# ---------- HYBRID RECOMMENDATION ----------
def hybrid_recommend(user_id, movie_title, top_n=5):
    content_recs = content_based_recommend(movie_title, 10)
    collab_recs = collaborative_recommend(user_id, 10)

    combined = pd.concat([content_recs, collab_recs]).drop_duplicates()
    return combined.head(top_n)['title'].tolist()

# ---------- TEST ----------
if __name__ == "__main__":
    print("Hybrid Recommendations:\n")
    print(hybrid_recommend(user_id=1, movie_title="Toy Story (1995)"))
