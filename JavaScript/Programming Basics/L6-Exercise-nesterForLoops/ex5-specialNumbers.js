function main(input)
{
    let number = Number(input[0]);
    let result = '';
    for (let index = 1111; index < 9999; index++)
    {
        let isSpecial = true;

        let num = index.toString();
        for (let i = 0; i < 4; i++)
            if (number % parseInt(num[i])  != 0)
            {
                isSpecial = false;
                break;
            }
        if (isSpecial)
            result += index + ' ';
    }
    console.log(result);
}

main([3]);
