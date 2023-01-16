function playSong(songsCollection, playedSongs, songName) {
    let song = songsCollection.indexOf(songName);
    if (song > 0) {
        if (playedSongs.indexOf(songName) < 0) {
            playedSongs.push(songName);
            return `Played songs: ${playedSongs.join(', ')}`;
        } else {
            return `Play On Repeat ${songName}`;
        }
    } else {
        return undefined;
    }
}
module.exports = playSong;

//console.log(playSong(['Imagine', 'One', 'Hey Jude', 'Billie Jean'], ['Hey Jude'], 'Respect')) // undefined
// console.log(playSong(['Imagine', 'One', 'Hey Jude', 'Billie Jean', 'Respect'], ['Hey Jude'], 'Respect')) //Played songs: Hey Jude, Respect
// console.log(playSong(['Imagine', 'One', 'Hey Jude', 'Respect', 'Billie Jean'], ['Hey Jude', 'Respect'], 'Respect')) //Play On Repeat Respect