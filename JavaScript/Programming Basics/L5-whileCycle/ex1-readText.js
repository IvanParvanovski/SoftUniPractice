function main(input)
{
    for (let index in input)
    {
        let element = input[index];
        if (element == 'Stop')
            break;
        console.log(element);
    }
}

main(["Nakov",
"SoftUni",
"Sofia",
"Bulgaria",
"SomeText",
"Stop",
"AfterStop",
"Europe",
"HelloWorld"]);
