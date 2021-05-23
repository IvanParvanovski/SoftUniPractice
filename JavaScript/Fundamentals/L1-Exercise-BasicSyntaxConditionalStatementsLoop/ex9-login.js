function checkUsername(data) {
    let i = 0;
    
    let realUsername = data[i];
    i++;

    for (; i < data.length; i++) {
        let current = data[i];
        let isCorrect = true;

        for (currentIndex = 0; currentIndex < current.length; currentIndex++) {
            if (!(current[currentIndex] == realUsername[realUsername.length - ++currentIndex])) {
                isCorrect = false;
                break;
            }
        }
        if (isCorrect) {
            console.log(`User ${realUsername} logged in.`);
            break;
        } else {
            if (i == data.length - 1) {
                console.log(`User ${realUsername} blocked!`);
            } else {
                console.log('Incorrect password. Try again.');
            }
        }
    }
}
checkUsername(['sunny','rainy','cloudy','sunny','not sunny']);
checkUsername(['momo','omom']);
