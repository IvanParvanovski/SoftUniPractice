function main(input)
{
    let budget = Number(input[0]);
    let statists = Number(input[1]);
    let statistClothingPrice = Number(input[2]);

    let clothingCost = statistClothingPrice * statists;
    let leftMoney = budget;

    leftMoney -= 0.1 * budget;
    
    if (statists > 150)
        clothingCost -= 0.1 * clothingCost;
    
    leftMoney -= clothingCost;

    let result;
    if (leftMoney >= 0)
        result = 'Action!\n' + 
                 `Wingard starts filming with ${leftMoney.toFixed(2)} leva left.`;
    else
        result = 'Not enough money!\n' +
                 `Wingard needs ${Math.abs(leftMoney).toFixed(2)} leva more.`;
    
    console.log(result);
}

main((["9587.88",
"222",
"55.68"])
);
