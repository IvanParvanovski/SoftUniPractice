const registerView = document.getElementById('register-view');
registerView.remove();

const loginView = document.getElementById('login-view');
loginView.remove();

const homeView = document.getElementById('home-view');
homeView.remove();

const main = document.querySelector('main');

const homeBtn = document.getElementById('home');
const loginBtn = document.getElementById('login')
const registerBtn = document.getElementById('register')
const logoutBtn = document.getElementById('logout')

homeBtn.addEventListener('click', onHome);
loginBtn.addEventListener('click', onLogin);
registerBtn.addEventListener('click', onRegister);
logoutBtn.addEventListener('click', onLogout);

onHome();

function onHome(event) {
    main.innerHTML = '';
    resetActivity();

    if (event != undefined) {
        event.target.className = 'active';
        event.preventDefault();
    } else {
        homeBtn.className = 'active';
    }

    main.appendChild(homeView);
}

function onLogin(event) { 
    main.innerHTML = '';
    resetActivity();   
    event.target.className = 'active';
    event.preventDefault();

    main.appendChild(loginView);

    loginView.querySelector('button').addEventListener('click', loginUser);
}

async function loginUser(event) {
    event.preventDefault();

    const emailField = loginView.querySelector('input[name="email"]');
    const passwordField = loginView.querySelector('input[name="password"]');

    const email = emailField.value;
    const password = passwordField.value;

    emailField.value = '';
    passwordField.value = '';

    const response = await fetch('http://localhost:3030/users/login', {
        method: 'post',
        headers: {'Content-Type': 'application/json', },
        body: JSON.stringify({email, password}),
    });

    if (response.ok) {
        const data = await response.json();
        
        const userData = {
            'email': data.email,
            'token': data.accessToken
        };

        sessionStorage.setItem('userData', JSON.stringify(userData));
        console.log(sessionStorage);

        onHome();
    }
}

function onRegister(event) {
    main.innerHTML = '';
    resetActivity();
    event.target.className = 'active'; 
    event.preventDefault();

    main.appendChild(registerView);

    registerView.querySelector('button').addEventListener('click', registerUser);
}

async function registerUser(event) {    
    event.preventDefault();

    const emailField = registerView.querySelector('input[name="email"]');
    const passwordField = registerView.querySelector('input[name="password"]');
    const rePasswordField = registerView.querySelector('input[name="rePass"]');

    const email = emailField.value;
    const password = passwordField.value;
    const rePass = rePasswordField.value;

    emailField.value = '';
    passwordField.value = '';
    rePasswordField.value = '';

    const response = await fetch('http://localhost:3030/users/register', {
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({email, password, rePass}),
        method: 'post'
    });

    if (response.ok) {
        const data = await response.json();
        const userData = {
            'email': data.email,
            'token': data.accessToken,
        };
        sessionStorage.setItem('userData', JSON.stringify(userData));
        console.log(JSON.parse(sessionStorage.getItem('userData')));

        onHome();
    } 
}

async function onLogout(event) {
    main.innerHTML = '';
    resetActivity();
    event.target.className = 'active'; 
    event.preventDefault();

    const userData = JSON.parse(sessionStorage.getItem('userData'));

    const response = await fetch('http://localhost:3030/users/logout',{
        headers: { 'X-Authorization': userData.token }
    })

    if (response.ok) {
        sessionStorage.removeItem('userData');
        console.log('logout successful!');

        onHome();
    }
}


function resetActivity() {
    homeBtn.className = '';
    loginBtn.className = '';
    registerBtn.className = '';
    logoutBtn.className = '';
}
