function stringSubstring(searchedWord, sentence) {
    console.log(
        sentence
            .toLowerCase()
            .indexOf(
                searchedWord.toLowerCase()) == -1 
                ? `${searchedWord} not found!` 
                : searchedWord
            );
}

stringSubstring('javascript',
'JavaScript is the best programming language')

stringSubstring('python',
'JavaScript is the best programming language')
