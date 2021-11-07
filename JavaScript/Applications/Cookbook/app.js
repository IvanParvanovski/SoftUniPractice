function cookbook() {    
    const mainElement = document.getElementsByTagName('main')[0];
    
    const userBtns = document.getElementById('user');
    const guestBtns = document.getElementById('guest');
    const logoutBtn = document.getElementById('logoutBtn');
    logoutBtn.addEventListener('click', onLogout);

    if (sessionStorage.token != null) {
        userBtns.style.display = 'inline';
        guestBtns.style.display = 'none';
    } else {
        userBtns.style.display = 'none';
        guestBtns.style.display = 'inline';
    }
    displayArticles();

    async function onLogout(event) {
        sessionStorage.removeItem('token');
        location.reload();
    }

    async function displayRecipe(event) {
        removePreviousRecipe();
        const id = this.id;
        const url = 'http://localhost:3030/data/recipes/' + id;
        const articleData = await getRequest(url);

        const newArticleDiv = document.createElement('article');
    
        const title = document.createElement('h2');
        title.textContent = articleData.name;

        // Band Div Elements
        const bandDiv = document.createElement('div');
        bandDiv.classList.add('band');

        // ThumbDiv Elements
        const thumbDiv = document.createElement('div');
        thumbDiv.classList.add('thumb');
        thumbDiv.innerHTML = `<img src="${articleData.img}">`;

        // Ingredients
        const ingredientsDiv = document.createElement('div');
        ingredientsDiv.classList.add('ingredients');
        ingredientsDiv.innerHTML = '<h3>Ingredients:</h3>';

        const ingredientsUl = document.createElement('ul'); 
        
        for (const ingredient of articleData.ingredients) {
            const li = document.createElement('li');
            li.textContent = ingredient;

            ingredientsUl.appendChild(li);
        }

        ingredientsDiv.appendChild(ingredientsUl);

        // Append Sections 
        bandDiv.appendChild(thumbDiv);
        bandDiv.appendChild(ingredientsDiv);

        // Description Elements
        const descriptionDiv = document.createElement('div');
        descriptionDiv.classList.add('description');

        descriptionDiv.innerHTML = '<h3>Preparation:</h3>';
        
        for (const text of articleData.steps) {
            const paragraph = document.createElement('p');
            paragraph.textContent = text;

            descriptionDiv.appendChild(paragraph);
        }
        
        newArticleDiv.appendChild(bandDiv);
        newArticleDiv.appendChild(descriptionDiv);

        mainElement.appendChild(newArticleDiv);
    }

    function removePreviousRecipe() {
        const lastArticle = mainElement.lastElementChild;
        if ([...lastArticle.classList].includes('preview')) {
            return;
        }

        mainElement.removeChild(lastArticle);
    }

    async function displayArticles() {
        const articles = await getRequest('http://localhost:3030/data/recipes?select=_id%2Cname%2Cimg');

        for (const article of articles) {
            const newArticle = document.createElement('article');
            newArticle.className = 'preview';
    
            newArticle.innerHTML = [
                '<div class="title">',
                    `<h2>${article.name}</h2>`,
                '</div>',
                '<div class="small">',
                    `<img src="${article.img}">`,
                '</div>'
            ].join('');

            newArticle.addEventListener('click', displayRecipe.bind({
                id: article._id
            }));

            mainElement.appendChild(newArticle);
        }
    }

    async function getRequest(url) {
        const response = await fetch(url);

        if (response.status != 200) {
            throw new Error(`Articles: ${response.status} ${response.statusText}`);
        }

        const data = await response.json();
        return data;
    }
}
