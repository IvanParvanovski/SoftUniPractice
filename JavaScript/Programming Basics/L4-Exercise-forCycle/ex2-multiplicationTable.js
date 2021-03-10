function main(input)
{
    let number = Number(input[0]);

    for (let i = 1; i < 11; i++)
        console.log(`${i} * ${number} = ${i * number}`);
}
main(['5']);