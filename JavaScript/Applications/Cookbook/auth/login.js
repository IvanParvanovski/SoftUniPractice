window.addEventListener('load', async () => {
    const form = document.querySelector('form');
    form.addEventListener('submit', onLogin);
});

async function onLogin(event) {
    event.preventDefault();
    const form = event.target;

    const url = 'http://localhost:3030/users/login';
    const formData = new FormData(form);
    
    const email = formData.get('email');
    const password = formData.get('password');

    const record = {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({email, password})
    };
    
    try {
        const response = await fetch(url, record);

        if (response.status == 403) {
            throw new Error('Wrong email or password!');
        } else if (response.ok == false) {
            throw new Error(`${response.status} ${response.statusText}`);
        }
        
        const result = await response.json();
        const token = result.accessToken;
        sessionStorage.setItem('token', token);

        form.reset();
        alert('Success!');
    } catch (error) {
        alert(error);
    }
} 

