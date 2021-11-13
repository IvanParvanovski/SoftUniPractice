window.addEventListener('load', (event) => {
    const logoutBtn = document.getElementById('logout');
    logoutBtn.addEventListener('click', logoutUser);
    
    const loadBtn = document.querySelector('.load');
    loadBtn.addEventListener('click', loadCatches);

    const addForm = document.querySelector('#addForm');
    addForm.addEventListener('submit', addCatch);

    displayButtons();
    loadCatches();
});

async function loadCatches() {
    const catchesSection = document.getElementById('catches'); 
    try {
        const catches = await request('http://localhost:3030/data/catches/');
        catchesSection.replaceChildren(...catches.map(c => createPreview(c)));
    } catch (err) {
        console.log(err);
        alert(err);
    }
}

async function addCatch(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    
    const data = [...formData.entries()].reduce((a, [k, v]) => Object.assign(a, {[k]: v}), {});
    data._ownerId = JSON.parse(sessionStorage.getItem('userData')).id;
    
    try {
        if (Object.values(data).some(x => x == '')) {
            throw new Error('Please fill in all field!');
        }

        const currentCatch = await request('http://localhost:3030/data/catches/', {
            method: 'post', 
            headers: {
                'X-Authorization': JSON.parse(sessionStorage.getItem('userData')).token,
            },
            body: JSON.stringify(data),
        });

        event.target.reset();
        loadCatches();
    } catch (err) {
        alert(err);
    }
}

function displayButtons() {
    const userData = JSON.parse(sessionStorage.getItem('userData'));

    if (userData == null) {
        document.querySelector('nav #user').style.display = 'none';
    } else {
        document.querySelector('nav #guest').style.display = 'none';
        document.querySelector('#addForm fieldset .add').disabled = false; 
    }
}

function createPreview(currentCatch) {
    const catchDiv = document.createElement('div');
    catchDiv.className = 'catch';
    catchDiv.addEventListener('click', onClickCatch);

    const activateResult = shouldActivateCatch(currentCatch);
    let activate = 'disabled';

    if (activateResult) {
        activate = '';
    }

    catchDiv.innerHTML = [
        '<label>Angler</label>',
        `<input type="text" class="angler" value="${currentCatch.angler}" ${activate}>`,
        '<label>Weight</label>',
        `<input type="text" class="weight" value="${currentCatch.weight}" ${activate}>`,
        '<label>Species</label>',
        `<input type="text" class="species" value="${currentCatch.species}" ${activate}>`,
        '<label>Location</label>',
        `<input type="text" class="location" value="${currentCatch.location}" ${activate}>`,
        '<label>Bait</label>',
        `<input type="text" class="bait" value="${currentCatch.bait}" ${activate}>`,
        '<label>Capture Time</label>',
        `<input type="number" class="captureTime" value="${currentCatch.captureTime}" ${activate}>`,
        `<button class="update" data-id="${currentCatch._id}" ${activate}>Update</button>`,
        `<button class="delete" data-id="${currentCatch._id}" ${activate}>Delete</button>`,
    ].join('');

    return catchDiv;
}

function onClickCatch(event) {
    if (event.target.tagName != 'BUTTON') {
        return;
    }

    const catchId = event.target.dataset.id;
    const userToken = JSON.parse(sessionStorage.getItem('userData')).token;
    const url =`http://localhost:3030/data/catches/${catchId}`;
    
    if (event.target.className == 'update') {
        const currentCatch = event.target.parentElement;
        const currentCatchData = [...currentCatch.querySelectorAll('input')].reduce((result, currentValue) => 
            Object.assign(result, {[currentValue.className]: currentValue.value}),
            {}
        );

        currentCatchData._ownerId = JSON.parse(sessionStorage.getItem('userData')).id;

        request(url, {
            method: 'put',
            headers: {
                'X-Authorization': userToken,
            },
            body: JSON.stringify(currentCatchData)
        });
    } else {
        request(url, {
            method: 'delete',
            headers: {
                'X-Authorization': userToken,
            },
        });
    }

    loadCatches();
}

function isUserLogged() {
    const user = sessionStorage.getItem('userData');
    return user != null;
}

function shouldActivateCatch(currentCatch) {
    if (!isUserLogged()) { return false };
    
    const user = sessionStorage.getItem('userData');
    return currentCatch._ownerId == JSON.parse(user).id;
}

async function request(url, options) {
    if (options && options.method == 'post') {
        if (options.hasOwnProperty('headers')) {
            Object.assign(options.headers, {
                'Content-Type': 'application/json',
            })
        } else {
            Object.assign(options, {
                headers: {'Content-Type': 'application/json',
            }})
        }
    }

    const response = await fetch(url, options);

    if (response.ok == false) {
        throw new Error(`${response.status} ${response.statusText}`);
    }

    const result = await response.json();
    return result;
}

function logoutUser(event) {
    sessionStorage.removeItem('userData');
    location.reload();
}
