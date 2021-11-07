window.addEventListener('load', async () => {
    const form = document.querySelector('form');
    form.addEventListener('submit', onRegister);
});

async function onRegister(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);

    const email = formData.get('email').trim();
    const password = formData.get('password').trim();
    const repeatPassword = formData.get('rePass').trim();

    try {
        if (password != repeatPassword) {
            throw new Error('Both passwords are not matching!')
        }  
        
        const url = 'http://localhost:3030/users/register';
        const record = {
            method: 'post',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({email, password})
        };

        const response = await fetch(url, record);
        
        if (response.ok == false) {
            const error = await response.json();
            throw new Error(`${response.status} ${response.statusText} ${error}`);
        }

        const result = await response.json();
        sessionStorage.setItem('token', result.accessToken);
        
        form.reset();
        alert('Success!');
    } catch (error) {
        alert(error);
    }

}
