function main(input)
{
    let numbersCount = Number(input[0]);
    
    percentage = {
        'p1': 0,
        'p2': 0,
        'p3': 0,
    };

    for (let i = 1; i <= numbersCount; i++)
    {
        let number = Number(input[i]);
        if (number % 2 == 0)
            percentage['p1']++;
        
        if (number % 3 == 0)
            percentage['p2']++;
        
        
        if (number % 4 == 0)
            percentage['p3']++;
    }

    for (let key in percentage)
        console.log((percentage[key] / numbersCount * 100).toFixed(2) + '%');
}

main([3, 3, 6, 9]);