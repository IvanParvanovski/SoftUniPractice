function main(input)
{
    let user = input[0];
    let password = input[1];

    for (let index = 1; index < input.length; index++)
        if (input[index] == password)
            break;
    
    console.log(`Welcome ${user}!`);
}

main(["Gosho",
"secret",
"secret"]);