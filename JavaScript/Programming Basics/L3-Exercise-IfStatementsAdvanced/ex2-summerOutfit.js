function main(input)
{
    let outfit;
    let shoes;

    let degrees = Number(input[0]);
    let dayTime = input[1];

    switch (dayTime)
    {
        case 'Morning':
            if (10 <= degrees && degrees <= 18)
            {
                outfit = 'Sweatshirt';
                shoes = 'Sneakers';
            }
            else if (degrees <= 24)
            {
                outfit = 'Shirt';
                shoes = 'Moccasins';
            }
            else
            {
                outfit = 'T-Shirt';
                shoes = 'Sandals'
            }
            break;
        
        case 'Afternoon':
            if (10 <= degrees && degrees <= 18)
            {
                outfit = 'Shirt';
                shoes = 'Moccasins';
            }
            else if (degrees <= 24)
            {
                outfit = 'T-Shirt';
                shoes = 'Sandals';
            }
            else
            {
                outfit = 'Swim Suit';
                shoes = 'Barefoot'
            }
            break;
        
        case 'Evening':
            if (10 <= degrees && degrees <= 18)
            {
                outfit = 'Shirt';
                shoes = 'Moccasins';
            }
            else if (degrees <= 24)
            {
                outfit = 'Shirt';
                shoes = 'Moccasins';
            }
            else
            {
                outfit = 'Shirt';
                shoes = 'Moccasins'
            }
            break;
    } 

    console.log(`It's ${degrees} degrees, get your ${outfit} and ${shoes}.`);
}
