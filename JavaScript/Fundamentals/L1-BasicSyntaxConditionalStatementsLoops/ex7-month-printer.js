function monthAsText(month) {
    let result;

    switch (month) {
        case 1:
            result = 'January';
            break;
    
        case 2:
            result = 'February';
            break;
    
        case 3:
            result = 'March';
            break;
    
        case 4:
            result = 'April';
            break;
    
        case 5:
            result = 'May';
            break;
    
        case 6:
            result = 'June';
            break;
    
        case 7:
            result = 'July';
            break;
    
        case 8:
            result = 'August';
            break;    
    
        case 9:
            result = 'September';
            break;
    
        case 10:
            result = 'October';
            break;
    
        case 11:
            result = 'November';
            break;
        
        case 12:
            result = 'December';
            break;
        
        default:
            result = 'Error!'
            break;
    }
    console.log(result);
}

monthAsText(1);
monthAsText(2);
monthAsText(3);
monthAsText(4);
monthAsText(5);
monthAsText(6);
monthAsText(7);
monthAsText(8);
monthAsText(9);
monthAsText(10);
monthAsText(11);
monthAsText(12);

monthAsText(13);
monthAsText(-1);
monthAsText(0);
