function main(input)
{
    let fruit = input[0];
    let day = input[1];
    let quantity = Number(input[2]);

    let workingDays = {
        'banana': 2.50,
        'apple': 1.20,
        'orange': 0.85,
        'grapefruit': 1.45,
        'kiwi': 2.70,
        'pineapple': 5.50,
        'grapes': 3.85,
    }

    let weekends = {
        'banana': 2.70,
        'apple': 1.25,
        'orange': 0.90,
        'grapefruit': 1.60,
        'kiwi': 3.00,
        'pineapple': 5.60,
        'grapes': 4.20
    } 

    let result;

    switch(day)
    {
        case 'Monday':
        case 'Tuesday':
        case 'Wednesday':
        case 'Thursday':
        case 'Friday':
            if (fruit in workingDays)
                result = workingDays[fruit] * quantity;
            else
                result = 'error';
            break;
        
        case 'Saturday':
        case 'Sunday':
            if (fruit in weekends)
                result = weekends[fruit] * quantity;
            else
                result = 'error';
            break;
        
        default:
            result = 'error';
            break;
    }
    console.log((result != 'error') ? result.toFixed(2) : result);
}

main(["apple",
"Tuesday",
"2"]);