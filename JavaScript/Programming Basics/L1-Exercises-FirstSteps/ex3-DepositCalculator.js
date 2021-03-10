function main(input)
{
    let depositSum = Number(input[0]);
    let depositTerm = Number(input[1]);
    let annualInterestPercent = Number(input[2]);
    
    let totalInteres = depositSum * annualInterestPercent / 100;
    let interestForMonth = totalInteres / 12;

    let total = depositSum + interestForMonth * depositTerm
    
    console.log(total)
}

main();
