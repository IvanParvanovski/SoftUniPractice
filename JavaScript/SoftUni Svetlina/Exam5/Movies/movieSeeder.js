class Movie {
    constructor(id, title, description, imageLocation) {
        this.id = id;
        this.title = title;
        this.description = description;
        this.imageLocation = imageLocation;
    }
}

const movies = [
    new Movie('1000100', 'Dead Poets Society (1989)', 'Set at a New England private school in 1959, this movie follows an English teacher, played by Robin Williams, and his relationship with his students as he teaches them to live a little more through poetry.', 'movie1000100'),
    new Movie('2000200', 'Jurassic Park (1993)', 'It\'s a little hard to believe that the Schindler\'s List director also came up with this dino adventure movie, but what\'s even more impressive is that the two films came out mere months apart.', 'movie2000200'),
    new Movie('3000300', 'Annihilation (2018)', 'Based very, very loosely on the book of the same name, Natalie Portman is a scientist who goes in search of her husband. She enters Area X, a mutated, trippy landscape that\'s been expanding ever since it was hit by a meteorite.', 'movie3000300'),
];

export {
    movies
};