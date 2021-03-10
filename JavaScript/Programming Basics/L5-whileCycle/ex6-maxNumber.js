function main(input)
{
    let maxNumber = Number.MIN_SAFE_INTEGER;
    for (let index in input)
    {
        let currentInput = input[index];
        if (currentInput == 'Stop')
            break;

        let currentNum = Number(currentInput);
        if (currentNum > maxNumber)
            maxNumber = currentInput; 
    } 
    console.log(maxNumber);
}

main(["-1",
"99",
"80",
"70",
"Stop"]);