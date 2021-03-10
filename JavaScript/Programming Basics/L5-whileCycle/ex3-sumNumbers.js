function main(input)
{
    
    let num = Number(input[0]);
    let total = 0;

    let index = 1;
    for (let index = 1; index < input.length; index++)
    {
        if (total >= num)
            break;
        total += Number(input[index]);
    }

    console.log(total);
}

main(["20",
"1",
"2",
"3",
"4",
"5",
"6"]);
