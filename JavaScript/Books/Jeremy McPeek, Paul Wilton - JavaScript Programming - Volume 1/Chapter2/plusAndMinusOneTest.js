function main() 
{
    let myVar1 = 2; 
    let myVar2 = myVar1++;

    console.log(myVar1);
    console.log(myVar2);

    let myVar3 = 2;
    let myVar4 = ++myVar3;

    console.log(myVar3);
    console.log(myVar4);

    let myNumber1 = 10;
    console.log(myNumber1++ * 10 + 1);
    console.log(myNumber1);

    let myNumber2 = 10;
    console.log(++myNumber2 * 10 + 1);
    console.log(myNumber2);
}

main();
