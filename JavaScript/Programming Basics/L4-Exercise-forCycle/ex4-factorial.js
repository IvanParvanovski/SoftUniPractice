function main(input)
{
    let number = Number(input[0]);

    let result = 1;
    for (let i = 1; i <= number; i++)
        result *= i;
    console.log(result);
}
main(['4']);