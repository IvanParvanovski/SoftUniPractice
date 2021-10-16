function lockedProfile() {
    const showProfileInfoButtons = Array.from(document.querySelectorAll('.profile button'));
    showProfileInfoButtons.forEach((x) => x.addEventListener('click', onToggle));
    
    function onToggle(event) {
        const clickedButton = event.target;
        const profile = clickedButton.parentElement;
        const isActive = profile.querySelector('input[type="radio"][value="unlock"]').checked;
        
        if (isActive) {
            const hiddenFieldElement = profile.querySelector('div');

            if (event.target.textContent  == 'Show more') {
                hiddenFieldElement.style.display = 'block';
                event.target.textContent = 'Hide it';
            } else if (event.target.textContent  == 'Hide it'){
                hiddenFieldElement.style.display = 'none';
                event.target.textContent = 'Show more';
            }
        }
    }
}