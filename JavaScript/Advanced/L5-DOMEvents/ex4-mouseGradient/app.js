function attachGradientEvents() {
    const gradient = document.getElementById('gradient');
    gradient.addEventListener('mousemove', onMove);
    const output = document.getElementById('result');

    function onMove(event) {
        const box = event.target;
        const offset = Math.floor(event.offsetX / box.clientWidth * 100);

        output.textContent = `${offset}%`;
    }
}