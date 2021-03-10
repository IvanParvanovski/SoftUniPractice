function main(input)
{
    let day = input[0];
    let result;
    switch(day)
    {
        case 'Monday':
        case 'Tuesday':
        case 'Wednesday':
        case 'Thursday':
        case 'Friday':
            result = 'Working day';
            break;
        case 'Saturday':
        case 'Sunday':
            result = 'Weekend';
            break;
        default:
            result = 'Error';
            break;
    }

    console.log(result);
}

main(['Monday']);
