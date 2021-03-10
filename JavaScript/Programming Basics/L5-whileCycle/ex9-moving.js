function main(input)
{
    let freeSpaceWidth = Number(input[0]);
    let freeSpaceLength = Number(input[1]);
    let freeSpaceHeigth = Number(input[2]);

    let volume = freeSpaceHeigth * freeSpaceWidth * freeSpaceLength;
    
    let boxesVolume = 0;
    let noMoreSpace = false;

    for (let i = 3; i < input.length; i++)
    {
        let currentInput = input[i];
        if (currentInput == 'Done')
            break;
        
        boxesVolume += Number(currentInput);

        if (boxesVolume > volume)
        {
            noMoreSpace = true;
            break;
        }
    }

    let result;
    let spaceDiff = Math.abs(volume - boxesVolume);
    
    if (noMoreSpace)
        result = `No more free space! You need ${spaceDiff} Cubic meters more.`;
    else
        result = `${spaceDiff} Cubic meters left.`;
    
        console.log(result);
}

main(["10",
"1",
"2",
"4",
"6",
"Done"]);