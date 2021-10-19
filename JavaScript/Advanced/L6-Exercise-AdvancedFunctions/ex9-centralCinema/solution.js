function solve() {
    const addMovieSection = document.querySelector('#add-new');
    const archiveSection = document.querySelector('#archive');
    const movieSection = document.querySelector('#movies ul');
    const archiveSectionMovies = archiveSection.querySelector('ul');

    addMovieSection
        .querySelector('#container button')
        .addEventListener('click', addNewMovie);

    archiveSection
        .querySelector('button')
        .addEventListener('click', clearArchive);

    function addNewMovie(event) {
        event.preventDefault();
        const parentElement = event.target.parentElement;
        const inputFields = [...parentElement.querySelectorAll('input')];

        const name = inputFields[0].value;
        const hall = inputFields[1].value;
        const ticketPrice = inputFields[2].value;
        
        if (isUserDataInvalid(name, hall, ticketPrice)) {
            return;
        }

        if (Number(ticketPrice) < 0) {
            return;
        }

        const newMovie = document.createElement('li');
        newMovie.innerHTML = `<span>${name}</span>` +
                             `<strong>Hall: ${hall}</strong>`;

        const priceDiv = document.createElement('div');
        priceDiv.innerHTML = `<strong>${Number(ticketPrice).toFixed(2)}</strong>` +
                             `<input placeholder="Tickets Sold">` +
                             `<button>Archive</button>`;

        const dataObj = {
            newMovie,
            name,
            ticketPrice,
        };
        
        priceDiv
            .querySelector('button')
            .addEventListener('click', e => archiveMovie.call(dataObj, e));
        
        inputFields.map((i) => i.value = '');
        newMovie.appendChild(priceDiv);
        movieSection.appendChild(newMovie);
    } 

    function archiveMovie(event) {
        const ticketsAmount = event.target.parentElement.querySelector('input').value;

        if (ticketsAmount.length == 0 || isNaN(ticketsAmount)){
            return;
        }

        if (Number(ticketsAmount.value) < 0) {
            return;
        } 

        const ticketsCost = Number(ticketsAmount) * Number(this.ticketPrice);

        const newMovie = document.createElement('li');
        newMovie.innerHTML = `<span>${this.name}</span>` +
                             `<strong>Total amount: ${ticketsCost.toFixed(2)}</strong>` +
                             `<button>Delete</button>`;

        newMovie
            .querySelector('button')
            .addEventListener('click', e => deleteMovie.call(newMovie, e))

        archiveSectionMovies.appendChild(newMovie);
        this.newMovie.remove();
    }
    
    function deleteMovie(event) {
        this.remove();
    }

    function clearArchive(event) {
        const movies = archiveSectionMovies.querySelectorAll('li');
        movies.forEach(m => m.remove());
    }

    function isUserDataInvalid(name, hall, ticketPrice) {
        return name == "" 
            || hall == "" 
            || ticketPrice == "" 
            || isNaN(ticketPrice);
    } 
}

