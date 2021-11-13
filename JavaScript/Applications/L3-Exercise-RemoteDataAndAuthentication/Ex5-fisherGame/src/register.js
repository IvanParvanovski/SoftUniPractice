window.addEventListener('load', (event) => {
    const form = document.querySelector('#register-view #register');
    form.addEventListener('submit', onRegister);

    displayButtons();
});

async function onRegister(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);

    const email = formData.get('email');
    const password = formData.get('password');
    const repeatedPassword = formData.get('rePass');

    try {
        if (password != repeatedPassword) {
            throw new Error('Passwords do not match!');
        }
        
        const user = await registerUser({email, password});
        form.reset();
        alert('Success!');
        window.location = './index.html';
    } catch (error) {
        alert(error);
    }
}

async function registerUser(data) {
    const url = 'http://localhost:3030/users/register';

    const response = await fetch(url, {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });

    if (response.ok == false) {
        throw new Error(`${response.status} ${response.statusText}`);
    }

    const result = await response.json();
   
    const userData =  {
        email: result.email,
        id: result._id,
        token: result.accessToken,
    };

    sessionStorage.setItem('userData', JSON.stringify(userData)); 
    
    return result;
}

function displayButtons() {
    const userData = JSON.parse(sessionStorage.getItem('userData'));

    if (userData == null) {
        document.querySelector('nav #user').style.display = 'none';
    } else {
        document.querySelector('nav #guest').style.display = 'none';
    }
}