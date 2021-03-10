function main(input) 
{
    let priceForOneSquareRoot = 7.61;
    let price = priceForOneSquareRoot * input;
    let discount = 18 / 100 * price;
    let result = price - discount;
    
    console.log(`The final price is: ${result} lv.`);
    console.log(`The discount is: ${discount} lv.`);
}

main("550");