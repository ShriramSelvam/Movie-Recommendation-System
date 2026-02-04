# 🎬 Movie Recommendation System (Hybrid ML + Flask)

## 📌 Overview

The **Movie Recommendation System** is a machine learning–based web application that provides **personalized movie recommendations** to users.

It implements a **hybrid recommendation approach**, combining:
- **Content-Based Filtering** (movie features)
- **Collaborative Filtering** (user behavior)

The application is built using **Python, Machine Learning, and Flask**, with a clean and interactive frontend developed using **HTML, CSS, and JavaScript**.

---

## 🚀 Features

- ✅ Content-Based Filtering using movie genres  
- ✅ User-Based Collaborative Filtering using ratings data  
- ✅ Hybrid Recommendation System for improved accuracy  
- ✅ Flask-powered backend  
- ✅ Dropdown-based movie selection (prevents input errors)  
- ✅ Clean and responsive UI  
- ✅ Modular and scalable code structure  

---

## 🧠 Recommendation Techniques Used

### 1️⃣ Content-Based Filtering
- TF-IDF Vectorization on movie genres  
- Cosine Similarity for measuring movie similarity  
- Recommends movies similar to a selected movie  

### 2️⃣ Collaborative Filtering
- User–Movie rating matrix construction  
- Identifies similar users using Cosine Similarity  
- Recommends movies liked by similar users  

### 3️⃣ Hybrid Recommendation System
- Combines content-based and collaborative results  
- Enhances personalization and recommendation quality  

---

## 🛠️ Tech Stack

### Backend & Machine Learning
- Python  
- Flask  
- Pandas  
- NumPy  
- Scikit-learn  

### Frontend
- HTML  
- CSS  
- JavaScript  

### Dataset
- **MovieLens (Latest Small Dataset)**  
- Provided by **GroupLens Research**

---

## 📂 Project Structure
```
Movie-Recommendation-System/
│
├── app.py # Flask backend
├── src/
│ ├── content_based.py
│ ├── collaborative_filtering.py
│ └── hybrid_recommender.py
│
├── data/
│ ├── movies.csv
│ └── ratings.csv
│
├── templates/
│ └── index.html
│
├── static/
│ ├── style.css
│ └── script.js
│
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ShriramSelvam/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```
### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Run the Flask App
```bash
python app.py
```
### 4️⃣ Open in Browser
```cpp
http://127.0.0.1:5000/
```

## 👨‍💻 Author

- Shriram Selvam
