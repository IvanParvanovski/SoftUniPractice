const carouselImagesDiv = document.querySelector('#myCarousel .carousel-inner');
const carouselChildren = carouselImagesDiv.children;

const nextBtn = document.getElementsByClassName('carousel-control-next')[0];
const previousBtn = document.getElementsByClassName('carousel-control-prev')[0];

nextBtn.addEventListener('click', onNext);
previousBtn.addEventListener('click', onPrevious);

function onNext(event) {
    for (let i = 0; i < carouselChildren.length; i++) {
        const currentElement = carouselChildren[i];
        
        if ([...currentElement.classList].includes('active')) {
            let newIndex;
            
            if (i == carouselChildren.length - 1) {
                newIndex = 0;
            } else {
                newIndex = i + 1;
            }            

            currentElement.classList.remove('active');
            carouselChildren[newIndex].classList.add('active');

            break;
        }
    }
}

function onPrevious(event) {
    for (let i = 0; i < carouselChildren.length; i++) {
        const currentElement = carouselChildren[i];
        
        if ([...currentElement.classList].includes('active')) {
            let newIndex;
            
            if (i == 0) {
                newIndex = carouselChildren.length - 1;
            } else {
                newIndex = i - 1;
            }            

            currentElement.classList.remove('active');
            carouselChildren[newIndex].classList.add('active');

            break;
        }
    }
}


console.log(carouselImagesDiv.children);


