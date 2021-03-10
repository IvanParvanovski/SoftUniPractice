function main(input)
{
    let dogsCount = input[0];
    let otherAnimalCount = input[1];

    let sum = dogsCount * 2.50 + otherAnimalCount * 4;
    console.log(sum);
}

main("5", "4");