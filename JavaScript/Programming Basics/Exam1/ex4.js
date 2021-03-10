function main(input)
{
    let catsCount = Number(input[0]);
    let group1 = 0;
    let group2 = 0;
    let group3 = 0;

    let totalFood = 0;
    let foodQuantity;
    for (let i = 1; i < input.length; i++)
    {
        foodQuantity = Number(input[i]);
        totalFood += foodQuantity;

        if (foodQuantity >= 100 &&foodQuantity < 200)
            group1++;
        else if (foodQuantity < 300)
            group2++;
        else if (foodQuantity < 400)
            group3++;
    }

    let foodInKilos = totalFood / 1000;
    let foodCost = foodInKilos * 12.45;

    console.log(`Group 1: ${group1} cats.`);
    console.log(`Group 2: ${group2} cats.`);
    console.log(`Group 3: ${group3} cats.`);
    console.log(`Price for food per day: ${foodCost.toFixed(2)} lv.`);
}

main([6, 102, 236, 123, 399, 342, 222]);
