function main(input)
{
    let start = Number(input[0]);
    let end = Number(input[1]);
    let result = '';
    for (let num = start; num <= end; num++)
    {
        let numInString = num.toString();
        let sumEvenPostition = 0;
        let sumOddPosition = 0;
        for (let i = 0; i < 6; i++)
        {
            let digit = parseInt(numInString.charAt(i));
            if (i % 2 == 0)
                sumEvenPostition += digit;
            else
                sumOddPosition += digit;
        }

        if (sumOddPosition == sumEvenPostition)
            result += num + ' ';
    }
    console.log(result);
}

main(
    ["123456",
"124000"]
);
