const bar = document.getElementById('progress');
const btnEl = document.getElementById('buttonProgress'); 

btnEl.addEventListener('click', move)

function move(event) {
    let currentWidth = bar.getAttribute('aria-valuenow');
    bar.style.background = 'blue';
    console.log(bar.style);

    console.log(currentWidth);
    // console.log(currentVal);

    // while (currentVal < 100) {
    //     bar.style.width = currentWidth + 1;
    //     bar.aria-valuenow = currentVal + 1;
    // }
}

