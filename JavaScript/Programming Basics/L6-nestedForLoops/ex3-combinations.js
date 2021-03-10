function main(input)
{
    let num = Number(input[0]) + 1;
    let total = 0;
    for (let index = num; index > 0; index--)
        total += index;
    console.log(total);
    // let counter = 0;

    // for (let i = 0; i <= num; i++)
    //     for (let j = 0; j <= num; j++)
    //         for (let k = 0; k <= num; k++)
    //             if (i + j + k == num)
    //                 counter++;
    
    // console.log(counter);
}

main(['25']);