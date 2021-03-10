function main(input)
{
    let pieces = Number(input.shift()) * Number(input.shift());
    let guestsPieces = 0;
    let cakeFinished = false;

    for (let index in input)
    {
        let data = input[index];
        if (data == 'STOP')
            break;

        guestsPieces += Number(data);
        if (guestsPieces > pieces)
        {
            cakeFinished = true;
            break;
        }
    }

    let result;
    if (cakeFinished)
        result = `No more cake left! You need ${guestsPieces - pieces} pieces more.`;
    else
        result = `${pieces - guestsPieces} pieces are left.`;
    
    console.log(result);
}

main(["10",
"2",
"2",
"4",
"6",
"STOP"]);
