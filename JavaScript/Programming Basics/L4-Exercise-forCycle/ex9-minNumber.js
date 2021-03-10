function main(input)
{
    let numbersCount = Number(input[0]);
    let smallestNumber = Number.MAX_VALUE;
    for (let i = 1; i <= numbersCount; i++)
    {
        let currentNum = Number(input[i]) ;
        if (currentNum < smallestNumber)
            smallestNumber = currentNum;
    }
    console.log(smallestNumber);
}
main();