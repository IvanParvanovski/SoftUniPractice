function toggle() {
    const buttonElement = document.getElementsByClassName('button')[0];
    const extraText = document.getElementById('extra');

    if (extraText.style.display == 'none' || extraText.style.display == '') {
        extraText.style.display = 'block';
        buttonElement.textContent = 'Less';
    } else {
        extraText.style.display = 'none';
        buttonElement.textContent = 'More';
    }
}