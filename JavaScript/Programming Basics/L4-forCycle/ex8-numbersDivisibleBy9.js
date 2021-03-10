function main(input)
{
    let firstNum = Number(input[0]);
    let secondNum = Number(input[1]);
    let total = 0;
    let result = [];
    for (let i = firstNum; i < secondNum; i++)
        if (i % 9 == 0)
        {
            total += i;
            result.push(i);
        }
    
    console.log(`The sum: ${total}`);
    console.log(result.join('\n'));
}

main(['100', '200']);