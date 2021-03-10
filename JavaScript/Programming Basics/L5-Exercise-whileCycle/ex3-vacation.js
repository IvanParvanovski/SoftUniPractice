function main(input)
{
    let neededMoney = Number(input.shift());
    let total = Number(input.shift());
    let spender = false;
    let spendCounter = 0;
    let days = 0;
    
    for (let index = 0; index < input.length; index += 2)
    {   
        if (total >= neededMoney)
            break;
        
        let action = input[index];
        let money = Number(index[index + 1]);
        switch(action)
        {
            case 'save':
                total += money;
                spendCounter = 0;
                break;

            case 'spend':
                total -= money;
                spendCounter++;
                break;
        }

        if (total < 0)
            total = 0;

        days++;
        if (spendCounter >= 5)
        {
            spender = true;
            break;
        }
    }
    let result;
    if (spender)
        result = `You can't save the money.\n${days}`;
    else
        result = `You saved the money for ${days} days.`;
    console.log(result);
}

main(["250",
"150",
"spend",
"50",
"spend",
"50",
"save",
"100",
"save",
"100"]);