function movies(input) {
    const movies = [];

    for (const mData of input) {
        if (mData.includes('addMovie')) {
            movies.push({ 
                name: mData.replace('addMovie', '').trim() 
            });
        } else if (mData.includes('directedBy')) {
            const [name, director] = mData.split(' directedBy ');
            const movie = movies.find(el => el.name == name);

            if (movie) {
                movie.director = director;
            }
        } else if (mData.includes('onDate')) {
            const [name, date] = mData.split(' onDate ');
            const movie = movies.find(el => el.name == name);
            
            if (movie) {
                movie.date = date;
            }
        }
    }

    for (const res of movies) {
        if (res.name && res.director && res.date) {
            console.log(JSON.stringify(res))
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
    'Fast and Furious directedBy Rob Cohen'
]);
