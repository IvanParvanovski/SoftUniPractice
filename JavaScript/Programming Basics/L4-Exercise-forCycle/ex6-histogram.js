function main(input)
{
    let numbersCount = Number(input[0]);
    
    let percentage = {
        'p1': 0,
        'p2': 0,
        'p3': 0,
        'p4': 0,
        'p5': 0,
    }

    for (let index = 1; index < input.length; index++)
    {
        let currentElement = Number(input[index]);

        if (currentElement < 200)
            percentage['p1']++;
        else if (currentElement < 400)
            percentage['p2']++;
        else if (currentElement < 600)
            percentage['p3']++;
        else if (currentElement < 800)
            percentage['p4']++;
        else
            percentage['p5']++;
    }

    for (var key in percentage)
        console.log((percentage[key] / numbersCount * 100).toFixed(2) + '%');
}

main(["3",
"1",
"2",
"999"]);