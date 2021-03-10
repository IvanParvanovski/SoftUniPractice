function main(input)
{
    // Hello is not a number, so - true
    console.log(isNaN(input[0]));

    // 54 is a number, so - false
    console.log(isNaN(input[1]));
}

main(['Hello', '54']);