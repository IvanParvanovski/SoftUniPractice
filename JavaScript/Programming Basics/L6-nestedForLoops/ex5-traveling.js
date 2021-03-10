function main(input)
{
    let index = 0
    while (true)
    {
        if (index >= input.length)
            break;
            
        let data = input[index];
        if (data == 'End')
            break;
        
        let country = data;
        index++;

        let neededMoney = Number(input[index]);
        index++;

        let total = 0;
        while (total < neededMoney)
        {
            total += Number(input[index]);
            index++;
        }
        console.log(`Going to ${country}!`);
    }
}
main(
    ["Greece",
"1000",
"200",
"200",
"300",
"100",
"150",
"240",
"Spain",
"1200",
"300",
"500",
"193",
"423",
"End"]
);