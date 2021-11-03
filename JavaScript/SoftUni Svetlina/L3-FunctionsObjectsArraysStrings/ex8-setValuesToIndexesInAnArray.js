function setValuesInArray( input )
{
    let count = input.shift();
    const result = [];

    for( const keyValuePair of input ) {
        const [index, value] = keyValuePair.split( ' - ' ).map( Number );
        result[index] = value;
    }

    for( let i = 0; i < count; i++ ) {
        let num = result[i];

        if (num == undefined) {
            num = 0;
        }

        console.log(num);
    }
}

// setValuesInArray([3, "0 - 5", "1 - 6", "2 - 7"]);
// setValuesInArray([2, "0 - 5", "0 - 6", "0 - 7"]);
// setValuesInArray([5, "0 - 3", "3 - -1", "4 - 2"]);

// console.log();


// function setIndex( text )
// {
//     let count = Number(text[0]);
//     let newArray = [];

//     for(let i = 1; i < text.length; i++ ) {
//         let [index, value] = text[i].split( ' - ' );
//         newArray[index] = value;
//     }

//     for(let j = 0; j < count; j++ ) {
//         console.log(newArray[j] == undefined ? 0 : newArray[j]);
//     }
// }