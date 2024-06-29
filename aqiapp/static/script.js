document.addEventListener('DOMContentLoaded', function() {
    const url = '/api/news/';

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const articles = data.articles;
            const newsContainer = document.getElementById('news-articles');
            
            if (articles.length === 0) {
                newsContainer.innerHTML = '<p>No air quality news articles found.</p>';
            } else {
                newsContainer.innerHTML = ''; // Clear previous content
                articles.forEach(article => {
                    const articleElement = document.createElement('div');
                    articleElement.className = 'article';
                    articleElement.innerHTML = `
                        <h3>${article.title}</h3>
                        <img src="${article.urlToImage || 'path_to_default_image.jpg'}" alt="${article.title}">
                        <p>${article.description}</p>
                        <a href="${article.url}" target="_blank">Read more</a>
                    `;
                    newsContainer.appendChild(articleElement);
                });
            }
        })
        .catch(error => {
            console.error('Error fetching air quality news:', error);
            const newsContainer = document.getElementById('news-articles');
            newsContainer.innerHTML = `<p>Error fetching air quality news: ${error.message}</p>`;
        });
});

