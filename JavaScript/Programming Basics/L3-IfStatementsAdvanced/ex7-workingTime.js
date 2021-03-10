function main(input)
{
    let time = Number(input[0]);
    let day = input[1];

    let result;

    switch(day)
    {
        case 'Monday':
        case 'Tuesday':
        case 'Wednesday':
        case 'Thursday':
        case 'Friday':
        case 'Saturday':
            if (time > 18 || time < 10)
                result = 'closed';
            else
                result = 'open';
            break;
        case 'Sunday':
            result = 'closed';
            break;
    }
    console.log(result);
}

