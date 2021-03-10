function main(input)
{
    let searchedBook = input.shift();
    let isFound = false;
    let foundIndex;

    for (let i = 0; i < input.length; i++)
    {
        let currentBook = input[i]; 
        
        if (currentBook == 'No More Books')
        {
            foundIndex = i;
            break;
        }

        else if (currentBook == searchedBook)
        {
            isFound = true;
            foundIndex = i;
            break;
        }
    }
    let result;
    if (isFound)
        result = `You checked ${foundIndex} books and found it.`;
    else
        result = 'The book you search is not here!\n' +
                 `You checked ${foundIndex} books.`;
    
    console.log(result);
}

main(["The Spot",
"Hunger Games",
"Harry Potter",
"Torronto",
"Spotify",
"No More Books"])
