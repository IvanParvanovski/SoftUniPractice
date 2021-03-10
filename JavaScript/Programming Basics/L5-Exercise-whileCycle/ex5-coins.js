function main(input)
{
    let diff = Number(input[0]) * 100;
    let coins = 0;
    while (true)
    {
        if (diff <= 0)
            break;

        if (diff - 200 >= 0)
            diff -= 200;
        else if (diff - 100 >= 0)
            diff -= 100;
        else if (diff - 50 >= 0)
            diff -= 50;
        else if (diff - 20 >= 0)
            diff -= 20;
        else if (diff - 10 >= 0)
            diff -= 10;
        else if (diff - 5 >= 0)
            diff -= 5;
        else if (diff - 2 >= 0)
            diff -= 2;
        else if (diff - 1 >= 0)
            diff -= 1;
        else
            break;
        coins++;
    }
    console.log(coins);
}
main(['0.59']);