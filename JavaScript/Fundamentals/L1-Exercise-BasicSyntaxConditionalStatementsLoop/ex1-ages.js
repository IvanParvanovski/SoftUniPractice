function determinesPerson(age) {
    let result;

    if (0 <= age && age <= 2) {
        result = 'baby';
    } else if (3 <= age && age <= 13) {
        result = 'child';
    } else if (14 <= age && age <= 19) {
        result = 'teenager';
    } else if (20 <= age && age <= 65) {
        result = 'adult';
    } else if (age >= 66) {
        result = 'elder';
    } else {
        result = 'out of bounds';
    }
    console.log(result);
}

determinesPerson(0);
determinesPerson(1);
determinesPerson(2);

determinesPerson(3);
determinesPerson(12);
determinesPerson(13);

determinesPerson(14);
determinesPerson(15);
determinesPerson(19);

determinesPerson(20);
determinesPerson(25);
determinesPerson(65);

determinesPerson(66);
determinesPerson(102);

determinesPerson(-5);
