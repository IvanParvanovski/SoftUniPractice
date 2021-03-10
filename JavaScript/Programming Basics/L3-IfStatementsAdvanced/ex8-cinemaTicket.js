function main(input)
{
    let day = input[0];
    let result;
    switch (day)
    {
        case 'Monday':
        case 'Tuesday':
        case 'Friday':
            result = 12;
            break;
        case 'Wednesday':
        case 'Thursday':
            result = 14;
            break;
        case 'Saturday':
        case 'Sunday':
            result = 16;
            break;
    }
    console.log(result);
}