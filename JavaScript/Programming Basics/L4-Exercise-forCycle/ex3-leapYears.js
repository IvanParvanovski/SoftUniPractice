function main(input)
{
    let startYear = Number(input[0]);
    let finalYear = Number(input[1]);

    for (let i = startYear; startYear <= finalYear; startYear += 4)
        console.log(startYear);
}

main([2000, 2008]);