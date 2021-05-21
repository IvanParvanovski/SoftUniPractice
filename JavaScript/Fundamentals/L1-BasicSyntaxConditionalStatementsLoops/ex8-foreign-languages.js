function spokenLanguage(country) {
    let result;
    
    switch (country) {
        case 'USA':
        case 'England':
            result = 'English';
            break;
        case 'Argentina':
        case 'Mexico':
        case 'Spain':
            result = 'Spanish';
            break;
        default:
            result = 'unknown';
            break;
    }

    console.log(result);
}

spokenLanguage('USA');
spokenLanguage('Argentina');
spokenLanguage('Mexico');
spokenLanguage('Spain');
spokenLanguage('Germany');
spokenLanguage('');
