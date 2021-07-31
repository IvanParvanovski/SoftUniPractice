function movies(input) {
    function getMovieAndOtherInformation(array, stop) {
        let movieNameData = [];
        let otherData = [];
        let arrayToAdd = movieNameData;

        for (let token of array) {
            if (token == stop) {
                arrayToAdd = otherData;
                continue;
            }
            arrayToAdd.push(token);
        }
        
        let movieName = movieNameData.join(' ');
        let otherInformation = otherData.join(' ');

        return [movieName, otherInformation];
    }

    function findMovie(array, name) {
        return array.find(x => x.name == name);
    }

    let films = [];

    for (let filmInfo of input) {
        let movieData = filmInfo.split(' ');
        
        let movieName;
        let movie;
        let movieIndex;

        if (movieData.includes('addMovie')) {
            [command,  ...movieName] = movieData;
            films.push({
                name: movieName.join(' '),
            });

        } else if (movieData.includes('directedBy')) {
            let directorName;
            [movieName, directorName] = getMovieAndOtherInformation(movieData, 'directedBy');
            movie = findMovie(films, movieName);

            if (movie) {
                movie['director'] = directorName;
            }

        } else if (movieData.includes('onDate')) {
            let date;
            [movieName, date] = getMovieAndOtherInformation(movieData, 'onDate');
            movie = findMovie(films, movieName);

            if (movie) {
                movie['date'] = date; 
            }
        }
    }

    for (let film of films) {
        let filmKeys = Object.keys(film);

        if (filmKeys.includes('name') &&
            filmKeys.includes('director') &&
            filmKeys.includes('date')) {
            
            console.log(JSON.stringify(film));
        }
    }
}

movies([
    'addMovie Fast and Furious',
    'addMovie Godfather',
    'Inception directedBy Christopher Nolan',
    'Godfather directedBy Francis Ford Coppola',
    'Godfather onDate 29.07.2018',
    'Fast and Furious onDate 30.07.2018',
    'Batman onDate 01.08.2018',
    'Fast and Furious directedBy Rob Cohen',
]);
