function main(input)
{
    let age = Number(input[0]);
    let gender = input[1];
    let result;
    switch (gender)
    {
        case 'm':
            if (age < 16)
                result = 'Master';
            else
                result = 'Mr.'
            break;
        
        case 'f':
            if (age < 16)
                result = 'Miss';
            else
                result = 'Ms.';
            break;
    }
    console.log(result);
}

main(['12', 'f']);