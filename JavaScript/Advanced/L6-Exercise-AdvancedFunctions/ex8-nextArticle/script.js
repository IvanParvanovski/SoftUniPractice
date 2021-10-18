function getArticleGenerator(articles) {
    const contentDiv = document.getElementById('content');

    function displayArticle() {
        if (articles.length == 0) {
            return;
        }

        const newArticle = document.createElement('article');
        const newArticleText = articles.shift();
        newArticle.textContent = newArticleText;
        
        contentDiv.appendChild(newArticle);
    }

    return displayArticle; 
}
