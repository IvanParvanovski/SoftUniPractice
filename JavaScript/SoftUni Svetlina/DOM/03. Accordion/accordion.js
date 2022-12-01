function toggle() {
    const info = document.getElementById('extra');
    const btn = document.getElementsByClassName('button')[0];

    if (btn.textContent.toLowerCase() == 'more') {
        info.style.display = 'block';
        btn.textContent = 'Less';

    } else if (btn.textContent.toLowerCase() == 'less') {
        info.style.display = 'none';
        btn.textContent = 'More'
    }
}