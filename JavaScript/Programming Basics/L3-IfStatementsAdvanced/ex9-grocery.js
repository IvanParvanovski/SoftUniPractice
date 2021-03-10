function main(input)
{
    let product = input[0];

    let fruits = [
        'banana', 
        'apple', 
        'kiwi', 
        'cherry', 
        'lemon', 
        'grapes'
    ];

    let vegetables = [
        'tomato',
        'cucumber',
        'pepper',
        'carrot'
    ]

    let result;
    if (fruits.includes(product))
        result = 'fruit';
    else if (vegetables.includes(product))
        result = 'vegetable';
    else
        result = 'unknown';
    
    console.log(result);
}