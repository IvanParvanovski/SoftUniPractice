function main(input)
{
    let total = 0;
    for (let i = 0; i < input.length; i++)
    {
        let currentInput = input[i];
        
        if (currentInput < 0)
        {
            console.log('Invalid operation!');
            break;
        }
        else if (currentInput == 'NoMoreMoney')
        {
            break;
        }
        
        let increase = Number(currentInput)
            console.log(`Increase: ${increase.toFixed(2)}`);
        total += increase;
    } 

    console.log(`Total: ${total.toFixed(2)}`);
}

main(["5.51", 
"69.42",
"100",
"NoMoreMoney"]);
