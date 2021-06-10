function diskRotations(band, album, song) {
    let songDuration = album.length * band.length * song.length / 2;
    let rotations = Math.ceil(songDuration / 2.5);
    console.log(`The plate was rotated ${rotations} times.`);
}

diskRotations('Black Sabbath', 'Paranoid', 'War Pigs');
