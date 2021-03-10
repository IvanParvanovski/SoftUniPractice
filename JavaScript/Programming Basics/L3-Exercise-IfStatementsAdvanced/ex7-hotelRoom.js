function main(input)
{
    let month = input[0];
    let nights = Number(input[1]);

    let apartmentPrice;
    let studioPrice;

    let discountApartment = 0;
    let discountStudio = 0;
    
    switch (month)
    {
        case 'October':
        case 'May':
            apartmentPrice = 65;
            studioPrice = 50;

            if (nights > 7)
                discountStudio = 0.05;

            if (nights > 14)
                discountStudio = 0.3;
            break;
        
        case 'June':
        case 'September':    
            apartmentPrice = 68.70;
            studioPrice = 75.20;

            if (nights > 14)
                discountStudio = 0.2;
            break;

        case 'July':
        case 'August':
            apartmentPrice = 77;
            studioPrice = 76;
            break;
    }

    if (nights > 14)
        discountApartment = 0.1;

    let apartmentCost = (apartmentPrice - apartmentPrice * discountApartment) * nights;
    let studioCost = (studioPrice - studioPrice * discountStudio) * nights;

    console.log(`Apartment: ${apartmentCost.toFixed(2)} lv.\n`
              + `Studio: ${studioCost.toFixed(2)} lv.`);
}

main(["May",
"0"]);