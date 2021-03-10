function main(input)
{
    let number = Number(input[0]);
    if (number < 100 && number != 0 || number > 200)
        console.log('invalid');
    
}

main(['0'])