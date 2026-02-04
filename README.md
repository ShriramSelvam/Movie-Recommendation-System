🎬 Movie Recommendation System (Hybrid ML + Flask)
📌 Overview

The Movie Recommendation System is a machine learning–based web application that provides personalized movie suggestions to users.
It combines content-based filtering and collaborative filtering techniques to recommend movies based on both movie attributes and user behavior.

The project is built using Python, Machine Learning, and Flask, with a clean web interface using HTML, CSS, and JavaScript.

🚀 Features

✅ Content-Based Filtering using movie genres

✅ User-Based Collaborative Filtering using ratings data

✅ Hybrid Recommendation System for better accuracy

✅ Flask-powered web application

✅ Dropdown-based movie selection (prevents input errors)

✅ Clean and responsive UI

✅ Modular and scalable code structure

🧠 Recommendation Techniques Used
1️⃣ Content-Based Filtering

Uses TF-IDF Vectorization on movie genres

Computes similarity using Cosine Similarity

Recommends movies similar to the user’s favorite movie

2️⃣ Collaborative Filtering

Builds a User–Movie Rating Matrix

Finds similar users using Cosine Similarity

Recommends movies liked by similar users

3️⃣ Hybrid Recommendation System

Combines results from both content-based and collaborative filtering

Improves personalization and recommendation quality

🛠️ Tech Stack
Backend & ML

Python

Flask

Pandas

NumPy

Scikit-learn

Frontend

HTML

CSS

JavaScript

Dataset

MovieLens (Latest Small Dataset)
Provided by GroupLens Research

📂 Project Structure
Movie-Recommendation-System/
│
├── app.py                     # Flask backend
├── src/
│   ├── content_based.py
│   ├── collaborative_filtering.py
│   └── hybrid_recommender.py
│
├── data/
│   ├── movies.csv
│   └── ratings.csv
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── requirements.txt
└── README.md

▶️ How to Run the Project Locally
1️⃣ Clone the Repository
git clone https://github.com/ShriramSelvam/Movie-Recommendation-System.git
cd Movie-Recommendation-System

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Flask App
python app.py

4️⃣ Open in Browser
http://127.0.0.1:5000/

🧪 Sample Usage

Enter User ID (e.g., 1)

Select a favorite movie from the dropdown

Click Get Recommendations

View personalized movie suggestions instantly

📈 Future Enhancements

🎯 Movie poster integration using external APIs

👤 User login and profile management

⭐ Rating predictions using Matrix Factorization (SVD)

🌐 Cloud deployment with CI/CD

📊 Recommendation evaluation metrics

👨‍💻 Author

Shriram Selvam

GitHub: https://github.com/ShriramSelvam

Interests: Full-Stack Development, Machine Learning, Software Engineering

⭐ If you like this project

Give it a ⭐ on GitHub — it really helps!