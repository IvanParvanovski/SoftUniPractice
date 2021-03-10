function main(input)
{
    let firstCompetitior = Number(input[0]);
    let secondCompetitior = Number(input[1]);
    let thirdCompetitior = Number(input[2]);

    let total = firstCompetitior + secondCompetitior + thirdCompetitior;
    let minutes = Math.trunc(total / 60);
    let leftSeconds = total % 60;

    if (leftSeconds < 10)
        console.log(`${minutes}:0${leftSeconds}`);
    else
        console.log(`${minutes}:${leftSeconds}`);
}

main(["35", "45", "44"]);
