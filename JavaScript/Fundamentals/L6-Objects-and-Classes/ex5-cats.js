function solve(cats) {
    class Cat {
        constructor(name, age) {
            this.name = name;
            this.age = age;
        }

        meow() {
            console.log(`${this.name}, age ${this.age} says Meow`);
        }
    };

    for (let cat of cats) {
        let catData = cat.split(' ');
        let [catName, catAge] = [catData[0], Number(catData[1])];
        
        let currentCat = new Cat(catName, catAge);
        currentCat.meow();
    }
}

solve(['Mellow 2', 'Tom 5']);