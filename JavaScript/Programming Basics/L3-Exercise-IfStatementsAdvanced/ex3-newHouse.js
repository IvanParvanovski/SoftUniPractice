function main(input)
{
    let flowerType = input[0];
    let flowersQuantity = Number(input[1]);
    let budget = Number(input[2]);

    let flowersPrices = {
        'Roses': 5.00,
        'Dahlias': 3.80,
        'Tulips': 2.80,
        'Narcissus': 3.00,
        'Gladiolus': 2.50,
    }

    let total = flowersPrices[flowerType] * flowersQuantity;

    switch (flowerType)
    {
        case 'Roses':
            if (flowersQuantity > 80)
                total -= 0.1 * total;
            break;
        
        case 'Dahlias':
            if (flowersQuantity > 90)
                total -= 0.15 * total;
            break;
        
        case 'Tulips':
            if (flowersQuantity > 80)
                total -= 0.15 * total;
            break;

        case 'Narcissus':
            if (flowersQuantity < 120)
                total += 0.15 * total;
            break;
        
        case 'Gladiolus':
            if (flowersQuantity < 80)
                total += 0.2 * total;
            break;
    }

    let diff = budget - total;
    let result;
    if (diff >= 0)
        result = `Hey, you have a great garden with ${flowersQuantity} ` +
                 `${flowerType} and ${diff.toFixed(2)} leva left.`
    else
        result = `Not enough money, you need ${Math.abs(diff).toFixed(2)} leva more.`
    
    console.log(result);
}

main(["Narcissus",
"119",
"360"]);
