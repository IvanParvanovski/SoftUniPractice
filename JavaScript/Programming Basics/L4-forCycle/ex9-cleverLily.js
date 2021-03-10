function main(input)
{
    let lilyAge = Number(input[0]);
    let laundryMachicePrice = Number(input[1]);
    let toyPrice = Number(input[2]);
    
    let total = 0;
    let evenBirthdayMoney = 10;
    let toysCount = 0;

    for (let i = 1; i <= lilyAge; i++)
    {
        if (i % 2 != 0) 
        {
            toysCount++;
        }
        else 
        {
            total += evenBirthdayMoney;
            evenBirthdayMoney += 10;
            total--;
        }
    }
    total += toysCount * toyPrice;
    let diff = total - laundryMachicePrice;
    let result;
    if (diff >= 0)
        result = `Yes! ${diff.toFixed(2)}`;
    else
        result = `No! ${Math.abs(diff).toFixed(2)}`;

    console.log(result);
}

main(['10', '170', '6']);
