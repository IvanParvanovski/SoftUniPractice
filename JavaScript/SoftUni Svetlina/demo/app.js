const element = document.getElementById('download');

let width = 0;
let id = null;
let click = false;

function move() {
    if (!click) {
        click = true;

        id = setInterval(function () {
            width += 3.4;
            if (width > 100) {
                width = 0;
            }

            if (width % 100 === 0) {
                clearInterval(id);
                click = false;
            }

            element.style.width = `${width}%`;
            element.innerHTML = `${width.toFixed(1)}%`;
        }, 1000);
    }
}
