function getRecommendations() {
    const userId = document.getElementById("userId").value;
    const movieTitle = document.getElementById("movieTitle").value;

    fetch('/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            user_id: userId,
            movie_title: movieTitle
        })
    })
    .then(response => response.json())
    .then(data => {
        const results = document.getElementById("results");
        results.innerHTML = "";

        if (data.error) {
            results.innerHTML = `<li>${data.error}</li>`;
        } else {
            data.recommendations.forEach(movie => {
                const li = document.createElement("li");
                li.textContent = movie;
                results.appendChild(li);
            });
        }
    });
}
