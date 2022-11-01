const barElement = document.querySelector('#page-header .bar');
const barElements = document.querySelectorAll('#page-header .bar .nav-list__item');

function changeElementsStyle(clr) {
    for (let el of barElements) {
        el.style.color = clr;
    }
}

changeElementsStyle();

function changeBg() {
    var scrollValue = window.scrollY;

    if (scrollValue > 150) {
        barElement.style.background = '#fff';
        barElement.style.paddingTop = '12.5px';
        barElement.style.paddingBottom = '12.5px';

        changeElementsStyle(
            '#000',
        );
    }
    else {
        barElement.style.background = 'transparent';
        barElement.style.paddingTop = '25px';
        barElement.style.paddingBottom = '0';

        changeElementsStyle(
            '#fff',
        );
    }
}

window.addEventListener('scroll', changeBg)