// console.log(document.location.href)

// window.onload = cardHover



export function cardHover() {
    const cards = document.querySelectorAll('.card');

    for (const cd of cards) {
        const cardDesc = cd.querySelector('.desc')
        cardDesc.style.display = 'none';
    }

    for (const card of cards) {
        card.addEventListener('mouseenter', onHover);
    }
}


function onHover(event) {
    let card = event.target;

    while (card.className != 'card') {
        card = event.target.parentNode;
    }

    const desc = card.querySelector('.desc');
    desc.style.display = 'block'


    card.addEventListener('mouseleave', onLeave);
}

function onLeave(event) {
    let card = event.target;

    while (card.className != 'card') {
        card = event.target.parentNode;
    }

    const desc = card.querySelector('.desc');
    desc.style.display = 'none';

    card.removeEventListener('mouseleave', onLeave);

}
