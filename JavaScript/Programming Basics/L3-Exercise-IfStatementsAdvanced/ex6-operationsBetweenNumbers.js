function main(input)
{
    let firstNumber = Number(input[0]);
    let secondNumber = Number(input[1]);
    let operator = input[2];
    let result;
    
    switch (operator)
    {
        case '+':
            result = firstNumber + secondNumber;
            break;
   
        case '-':
            result = firstNumber - secondNumber;
            break;
    
        case '*':
            result = firstNumber * secondNumber;
            break;
    
        case '/':
            result = firstNumber / secondNumber;
            break;

        case '%':
            result = firstNumber % secondNumber;
            break;
    }

    let checkOperator = operator == '+' || operator == '-' || operator == '*';
    let checkEvenOrOdd = result % 2 == 0
    result = operator == '/' ? result.toFixed(2) : result;

    if (secondNumber == 0 && operator)
        console.log
        (
            `Cannot divide ${firstNumber} by zero`
        );
    else
        console.log
        (
            `${firstNumber} ${operator} ${secondNumber} = ${result}` 
            + (checkOperator ? (checkEvenOrOdd ? ' - even' : ' - odd') : '')
        );            
}

main(["10", "4", "-"]);