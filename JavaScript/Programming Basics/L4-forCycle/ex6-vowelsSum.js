function main(input)
{
    let vowels = {
        'a': 1,
        'e': 2,
        'i': 3,
        'o': 4,
        'u': 5,
    };

    let word = input[0];
    let total = 0;
    for (let index in word)
        total += word[index] in vowels ? vowels[word[index]] : 0;
    console.log(total);
} 

main(['hello']);