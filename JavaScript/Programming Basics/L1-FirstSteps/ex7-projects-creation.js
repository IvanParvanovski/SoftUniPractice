function main(input)
{
    let dict = {};
    let arr = [];
    let tuple = [];
    
    tuple.push('a');
    console.log(tuple);

    tuple = 'hi';
    console.log(tuple);

    let name = input[0];
    let projectsCount = input[1];

    console.log(`The architect ${name} will need ${projectsCount * 3} hours to complete ${projectsCount} project/s.`);
}

main(["George", "4"]);
