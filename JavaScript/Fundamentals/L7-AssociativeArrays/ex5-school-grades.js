function school(students) {
    function getAverage(array) {
        let total = 0;

        for (let number of array) {
            total += number;
        }

        return total / array.length;
    }

    let studentsGrades = {};

    for (let studentInfo of students) {
        let studentData = studentInfo.split(' ');
        let studentName = studentData.shift();
        let studentGrades = studentData.map(x => Number(x))

        if (studentName in studentsGrades) {
            studentsGrades[studentName].push(...studentGrades);
        } else {
            studentsGrades[studentName] = studentGrades; 
        }
    }

    let sortedStudents = Object.entries(studentsGrades)
        .sort((a, b) => getAverage(a[1]) - getAverage(b[1]));

    for (let scholar of sortedStudents) {
        console.log(`${scholar[0]}: ${scholar[1].join(', ')}`);
    }
}

school([
    'Lilly 4 6 6 5',
    'Tim 5 6',
    'Tammy 2 4 3',
    'Tim 6 6',
]);

