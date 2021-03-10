function main(input)
{
    let country = input[0];
    let trinket = input[1];
    let trinketCount = Number(input[2]);

    
    let items = {
        'Argentina': {
            'flags': 3.25,
            'caps': 7.20,
            'posters': 5.10,
            'stickers': 1.25,
        },

        'Brazil': {
            'flags': 4.20,
            'caps': 8.50,
            'posters': 5.35,
            'stickers': 1.20,
        },

        'Croatia': {
            'flags': 2.75,
            'caps': 6.90,
            'posters': 4.95,
            'stickers': 1.10,
        },

        'Denmark': {
            'flags': 3.10,
            'caps': 6.50,
            'posters': 4.80,
            'stickers': 0.90,
        },
    } 

    if (!(country in items))
        console.log('Invalid country!');
    else if (!(trinket in items[country]))
        console.log('Invalid stock!');
    else
    {
        let total = items[country][trinket] * trinketCount
        console.log(`Pepi bought ${trinketCount} ${trinket} of ${country} for ${total.toFixed(2)} lv.`);
    }
    
}

main(['Argentina', 'shirts', '8']);