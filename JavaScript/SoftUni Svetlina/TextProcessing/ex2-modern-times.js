function modernTimes(input) {
    console.log(input.match(/#(?<word>[A-Za-z]+)/g).map((el) => el.replace('#', '')).join('\n'));
}

modernTimes('Nowadays everyone uses # to tag a #special word in #socialMedia');
