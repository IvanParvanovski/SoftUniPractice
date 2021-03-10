function main(input)
{
    let hall = Number(input[0]);
    let cake = 20 / 100 * hall;
    let drinks = cake - 45 / 100 * cake;
    let funster = 1 / 3 * hall;

    console.log(cake + drinks + funster + hall);
}

main();
