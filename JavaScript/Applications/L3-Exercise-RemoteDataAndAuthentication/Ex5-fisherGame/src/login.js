window.addEventListener('load', (event) => {    
    const form = document.querySelector('#login-view #login');
    form.addEventListener('submit', onLogin);
    
    displayButtons();
});

async function onLogin(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);

    const email = formData.get('email');
    const password = formData.get('password');
    const fields = {email, password};
    
    try {
        if (Object.values(fields).some(x => x == '')) {
            throw new Error('Please fill in all fields!');
        }
        
        const user = await loginUser(fields);
        form.reset();
        alert('Success!');
        window.location = './index.html';
    } catch (error) {
        alert(error);
    }   
} 

async function loginUser(data) {
    const url = 'http://localhost:3030/users/login';

    const response = await fetch(url, {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    });

    if (response.status == 403) {
        throw new Error('The username or password is invalid!');
    } else if (response.ok == false) {
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