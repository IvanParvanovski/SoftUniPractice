function main()
{
    let myStr1 = 'Hello!';
    let myStr2 = myStr1;

    let myStr3 = new String('My name is ....');
    let myStr4 = myStr3;

    // let myStr5 = myStr5;

    console.log(myStr1);
    console.log(myStr2);
    console.log(myStr3);
    console.log(myStr4);
    // console.log(myStr5);

    myStr2 = 'No';
    myStr4.String = 'Yes';

    console.log(myStr1);
    console.log(myStr2);
    console.log(myStr3);
    console.log(myStr4);
    
}

main();