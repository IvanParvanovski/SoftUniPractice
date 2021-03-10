function main(input)
{
    let number = Number(input[0]);
    
    let current = 1;
    let isBigger = false;

    for (let row = 1; row <= number; row++)
    {
        let printCurrentLine = '';
        for (let col = 1; col <= row; col++)
        {
            if (current > number)
            {
                isBigger = true;
                break;
            }
            printCurrentLine += current + ' ';
            current++;
        }

        console.log(printCurrentLine);
        if (isBigger)
            break;
    }
}

main(['7']);
