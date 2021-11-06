// Добави си onload="solution()" в body тага (html) за да работи

// function solution() {
//     const mainSection = document.getElementById('main');
//     const articles = getArticles();

//     for (const article of articles) {
//         const newArticle = document.createElement('div');
//         newArticle.className = 'head';

//         const articleTitle = document.createElement('span');
//         articleTitle.textContent = article.title;

//         const articleBtn = document.createElement('button');
//         articleBtn.className = 'button';
//         articleBtn.id = article._id;
//         articleBtn.textContent = 'More';
//         articleBtn.addEventListener('click', onClick);

//         newArticle.appendChild(articleTitle);
//         newArticle.appendChild(articleBtn);
        
//         mainSection.appendChild(newArticle)
//     }

//     function onClick(event) {
        
//     }

//     async function getArticles() {
//         try {
//             const url = 'http://localhost:3030/jsonstore/advanced/articles/list';
//             const response = await fetch(url);
            
//             if (response.status != 200) {
//                 throw new Error('Invalid HTTP Request!');
//             }
            
//             const data = await response.json();
//             return data;
//         } catch (error) {
//             console.error(error);
//         }
//     }
// }