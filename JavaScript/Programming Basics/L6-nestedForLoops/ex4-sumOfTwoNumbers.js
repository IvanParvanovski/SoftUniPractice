function main(input)
{
    let start = Number(input[0]);
    let end = Number(input[1]);
    let targetNum = Number(input[2]);
    let isFound = false;
    let combination = 0;

    for (let i = start; i <= end; i++)
    {
        for (let j = start; j <= end; j++)
        {
            if (i + j == targetNum)
            {
                console.log(`Combination N:${combination + 1} (${i} + ${j} = ${targetNum})`);
                isFound = true;
                break;
            }
            combination++;
        }
        if (isFound)
            break;
    }

    if (!isFound)
        console.log(`${combination} combinations - neither equals ${targetNum}`);
}

main(['23', '24', 20]);