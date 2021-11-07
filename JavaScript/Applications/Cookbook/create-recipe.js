window.addEventListener('load', () => {
    const token = sessionStorage.getItem('token');
    
    if (token == null) {
        location.assign('/auth/login.html');
    }

    const form = document.querySelector('form');
    form.addEventListener('submit', createRecipe);
})

async function createRecipe(event) {
    const form = event.target;

    const formData = new FormData(form);
    const url = 'http://localhost:3030/data/recipes/';

    const name = formData.get('name').trim();
    const image = formData.get('img').trim();
    const ingredients = formData.get('ingredients').trim().split('\n');
    const steps = formData.get('steps').trim().split('\n');

    const token = sessionStorage.token;

    if (token == null) {
        location.assign('/auth/login.html');
        return;
    }

    const record = {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
            'X-Authorization': token
        },
        body: JSON.stringify({
            name,
            img: image,
            ingredients,
            steps,
        })
    };    

    try {
        const response = await fetch(url, record);

        if (response.ok == false) {
            throw new Error(`${response.status} ${response.statusText}`);
        }

        await response.json();
        location.assign('/index.html');
    } catch (error) {
        alert(error);
    }
    

}
