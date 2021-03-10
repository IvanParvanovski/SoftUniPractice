function main(input)
{
    let targetNum = Number(input[0]);
    let currentNum = 1;
    while (true)
    {
        if (currentNum > targetNum)
            break;
        
        console.log(currentNum);
        currentNum += currentNum + 1;
    }
}

main([3]);