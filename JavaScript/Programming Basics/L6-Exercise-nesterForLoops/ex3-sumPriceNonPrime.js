function main(input)
{
    let primeSum = 0;
    let nonPrimeSum = 0;

    for (let index in input)
    {
        let data = input[index]
        if (data == 'stop')
            break;
        
        let number = Number(data);
        if (number < 0)
        {
            console.log('Number is negative.');
            continue;
        }

        let prime = true;
        for (let i = 2; i < number; i++)
            if (number % i == 0)
            {
                prime = false;
                break;
            }

        if (prime)
            primeSum += number;
        else
            nonPrimeSum += number;
    }
    console.log(`Sum of all prime numbers is: ${primeSum}`);
    console.log(`Sum of all non prime numbers is: ${nonPrimeSum}`);
}
main(
    [3, 9, 0, 7, 19, 4]
);