async function lockedProfile() {
    const main = document.getElementById('main');
    const profiles = await (await fetch('http://localhost:3030/jsonstore/advanced/profiles')).json(); 
    let count = 0;

    for (const profileId in profiles) {
        count += 1;
        const profile = profiles[profileId];
        console.log(profile);

        const profileDiv = document.createElement('div');
        profileDiv.className = 'profile';

        profileDiv.innerHTML = [
            '<img src="./iconProfile2.png" class="userIcon" />',
            '<label>Lock</label>',
            `<input type="radio" name="user${count}Locked" value="lock">`,
            '<br>',
            '<label>Unlock</label>',
            `<input type="radio" name="user${count}Locked" value="unlock">`,
            '<br>',
            '<hr>',
            '<label>Username</label>',
            `<input type="text" name="user1Username" value="${profile.username}" disabled readonly/>`
        ].join('');

        profileDiv.children[2].checked = true;

        const hiddenDiv = document.createElement('div');
        hiddenDiv.id = 'user1HiddenFields';

        hiddenDiv.innerHTML = [
            '<label>Email:</label>',
            `<input type="email" name="user${count}Email" value="${profile.email}" disabled readonly />`,
            '<label>Age:</label>',
            `<input type="email" name="user${count}Age" value="${profile.age}" disabled readonly />`,
        ].join('');        

        const btn = document.createElement('button');
        btn.innerHTML = 'Show more';
        btn.addEventListener('click', onShow);

        profileDiv.appendChild(btn);

        profileDiv.appendChild(hiddenDiv);
        main.appendChild(profileDiv);
    }

    function onShow(event) {
        const additives = event.target.parentNode.lastChild;

        if (event.target.parentNode.children[5].checked) {
            if (event.target.innerHTML == 'Hide it') {
                event.target.innerHTML = 'Show more';
                additives.style.display = 'none';
            } else if (event.target.innerHTML == 'Show more') {
                event.target.innerHTML = 'Hide it';
                additives.style.display = 'block';
            }
            
        }
    }
}

