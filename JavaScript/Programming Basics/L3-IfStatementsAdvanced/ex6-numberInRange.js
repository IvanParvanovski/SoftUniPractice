function main(input)
{
    let number = Number(input[0]);
    let result;

    if (number >= -100 && number <= 100 && number != 0)
        result = 'Yes';
    else
        result = 'No';
    
    console.log(result);

}

main(['-25']);
main(['0']);
main(['25']);
