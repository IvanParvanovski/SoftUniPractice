function songs(input) {
    class Song {
        constructor(typeList, name, time) {
            this.typeList = typeList;
            this.name = name;
            this.time = time;
        }
    }
    
    let songsCount = Number(input.shift());
    let songs = [];

    for (let i = 0; i < songsCount; i++) {
        let songData = input[i].split('_');
        let song = new Song(songData[0], songData[1], songData[2]);
        songs.push(song);
    }

    let searchedType = input[input.length - 1];
    for (let song of songs) {
        if (song.typeList == searchedType || searchedType == 'all') {
            console.log(song.name);
        }
    }

}

songs([4,
    'favourite_DownTown_3:14',
    'listenLater_Andalouse_3:24',
    'favourite_In To The Night_3:58',
    'favourite_Live It Up_3:48',
    'listenLater']);