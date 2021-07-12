function solve(input) {
    let genres = input.shift().split(' | ');
    
    for (let commandData of input) {
        let commandTokens = commandData.split(' '); 
        let command = commandTokens[0];
        
        if (command == 'Stop!') {
            break;
        }

        let genre = commandTokens[1];

        switch (command) {
            case 'Join':
                if (!genres.includes(genre)) {
                    genres.push(genre);
                }
                break;
            
            case 'Drop':
                if (genres.includes(genre)) {
                    genres.splice(genres.indexOf(genre), 1);
                }
                break;

            case 'Replace':
                let newGengre = commandTokens[2]; 
                if (genres.includes(genre)) {
                    if (!genres.includes(newGengre)) {
                        genres.splice(genres.indexOf(genre), 1, newGengre);
                    }
                }
                break;
        }
    }
    console.log(genres.join(' '));
}

solve(['Thriller | Young | Crime', 'Join Political', 'Replace Young Fairytale', 'Stop!']);
