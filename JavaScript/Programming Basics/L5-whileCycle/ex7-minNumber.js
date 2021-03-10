function main(input)
{
    let minNumber = Number.MAX_SAFE_INTEGER;
    for (let index in input)
    {
        let currentInput = input[index];
        if (currentInput == 'Stop')
            break;

        let currentNum = Number(currentInput);
        if (currentNum < minNumber)
            minNumber = currentInput; 
    } 
    console.log(minNumber);
}
