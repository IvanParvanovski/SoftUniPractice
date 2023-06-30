class Student {
    constructor(name, points) {
        this.name = name;
        this.points = points;
    }
}

const students = [
    new Student('Maya', 600),
    new Student('Ryan', 550),
    new Student('Julia', 700),
];

export {
    students
};