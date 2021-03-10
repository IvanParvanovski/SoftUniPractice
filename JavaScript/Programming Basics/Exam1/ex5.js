function main(input)
{
    let peopleAndPresents = {
        'adults': 0,
        'kids': 0,
        'toys': 0,
        'sweates': 0,
    }

    for (let index in input)
    {
        let data = input[index];
        if (data == 'Christmas')
            break;
        
        let age = Number(data);
        if (age > 16)
        {
            peopleAndPresents['adults']++;
            peopleAndPresents['sweates']++;
        }
        else
        {
            peopleAndPresents['kids']++;
            peopleAndPresents['toys']++;
        }
    }

    console.log(`Number of adults: ${peopleAndPresents['adults']}`);
    console.log(`Number of kids: ${peopleAndPresents['kids']}`);
    console.log(`Money for toys: ${peopleAndPresents['toys'] * 5}`);
    console.log(`Money for sweaters: ${peopleAndPresents['sweates'] * 15}`);

}

main([16, 20, 46, 12, 8, 20, 49, 'Christmas']);
