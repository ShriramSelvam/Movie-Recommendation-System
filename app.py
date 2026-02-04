from flask import Flask, render_template, request, jsonify
from src.hybrid_recommender import hybrid_recommend
import pandas as pd

app = Flask(__name__)

# Load movie titles once
movies_df = pd.read_csv("data/movies.csv")
movie_titles = sorted(movies_df['title'].tolist())

@app.route('/')
def home():
    return render_template('index.html', movies=movie_titles)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    user_id = int(data['user_id'])
    movie_title = data['movie_title']

    try:
        recommendations = hybrid_recommend(user_id, movie_title)
        return jsonify({'recommendations': recommendations})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
