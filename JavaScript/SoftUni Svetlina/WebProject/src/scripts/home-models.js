export function hoverModels() {
    const models = document.getElementsByClassName('model');

    for (const model of models) {
        model.querySelector('.control-left').addEventListener('click', (ev) => onPreviousAlbum(ev, model));
        model.querySelector('.control-right').addEventListener('click', (ev) => onNextAlbum(ev, model));

        model.addEventListener('mouseover', onHoverModel)
        model.addEventListener('mouseout', onMouseOver);
    }

    function onHoverModel(event) {

        let modelDiv = event.target;

        while (modelDiv.className != 'model') {
            modelDiv = modelDiv.parentNode;
        }

        const img = modelDiv.querySelector('.model__img');
        const desc = modelDiv.querySelector('.model__desc');

        img.style.width = '50%';
        desc.style.display = 'flex';

        modelDiv.style.flex = 7;
    }

    function onMouseOver(event) {
        let modelDiv = event.target;

        while (modelDiv.className != 'model') {
            modelDiv = modelDiv.parentNode;
        }

        const desc = modelDiv.querySelector('.model__desc');
        const img = modelDiv.querySelector('.model__img');

        img.style.width = '100%';
        desc.style.display = 'none';

        modelDiv.style.flex = 1;

    }
}

function onPreviousAlbum(ev, modelDiv) {
    console.log('previous');
    const images = modelDiv.querySelectorAll('.albums img');

    for (let i = 0; i < images.length; i++) {
        const img = images[i];

        if (img.className == '--active') {
            let newIndex = i - 1;

            if (newIndex == -1) {
                newIndex = images.length - 1;
            }

            img.className = '';
            images[newIndex].className = '--active';

            return;
        }
    }
}

function onNextAlbum(ev, modelDiv) {
    console.log('next');
    const images = modelDiv.querySelectorAll('.albums img');

    for (let i = 0; i < images.length; i++) {
        const img = images[i];

        if (img.className == '--active') {
            let newIndex = i + 1;

            if (newIndex == images.length) {
                newIndex = 0;
            }

            img.className = '';
            images[newIndex].className = '--active';

            return;
        }
    }
}

