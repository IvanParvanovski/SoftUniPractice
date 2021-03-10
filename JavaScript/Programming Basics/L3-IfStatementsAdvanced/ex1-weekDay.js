function main(input)
{
    let day = Number(input[0]);
    let result;

    switch(day)
    {
        case 1:
            result = 'Monday';
            break;
        
        case 2:
            result = 'Tuesday';
            break;
        
        case 3:
            result = 'Wednesday';
            break;
                                
        case 4:
            result = 'Thursday';
            break;
        
        case 5:
            result = 'Friday';
            break;
        
        case 6:
            result = 'Saturday';
            break;
        
        case 7:
            result = 'Sunday';
            break;
        
        default:
            result ='Error';
            break;
    }

    console.log(result);
}

main(['1']);
main(['2']);
main(['3']);
main(['4']);
main(['5']);
main(['6']);
main(['7']);
main(['8']);

