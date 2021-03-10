function main(input)
{
    let number = Number(input[0]);
    let inputMetric = input[1];
    let outputMetric = input[2];

    let result;

    if (inputMetric == 'm')
    {
        if (outputMetric == 'mm')
            result = number * 1000;
        else if (outputMetric == 'cm')
            result = number * 100;
    }
    else if (inputMetric == 'cm')
    {
        if (outputMetric == 'm')
            result = number / 100;
        else if (outputMetric == 'mm')
            result = number * 10;
    }
    else if (inputMetric == 'mm')
    {
        if (outputMetric == 'm')
            result = number / 1000;
        else if (outputMetric == 'cm')
            result = number / 10;
    }

    console.log(result.toFixed(3));
}

main();
