from flask import Flask, render_template, request, jsonify
from src.hybrid_recommender import hybrid_recommend

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

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

if __name__ == '__main__':
    app.run(debug=True)
