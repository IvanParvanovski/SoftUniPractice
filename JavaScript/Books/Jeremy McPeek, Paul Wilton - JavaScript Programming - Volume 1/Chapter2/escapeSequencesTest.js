function main()
{
    let text1 = "123\b456";
    let text2 = "123\f456";
    let text3 = "123\n456";
    let text4 = "123\r456";
    let text5 = "123\t456";
    let text6 = "123\'456";
    let text7 = "123\"456";
    let text8 = "123\\456";
    let text9 = "123\xA9456";

    console.log(`Text 1: ${text1}`);
    console.log(`Text 2: ${text2}`);
    console.log(`Text 3: ${text3}`);
    console.log(`Text 4: ${text4}`);
    console.log(`Text 5: ${text5}`);
    console.log(`Text 6: ${text6}`);
    console.log(`Text 7: ${text7}`);
    console.log(`Text 8: ${text8}`);
    console.log(`Text 9: ${text9}`);

    
}

main();