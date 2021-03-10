function main(input)
{
    let daysCountCampaignTakesPlace = Number(input[0]);
    let confectionersCount = Number(input[1]);
    let cakesCount = Number(input[2]);
    let wafflesCount = Number(input[3]);
    let pancakesCount = Number(input[4]);

    let prices = {
        "cake": 45,
        "waffle": 5.80,
        "pancake": 3.20,
    };

    let cakesPrice = cakesCount * prices["cake"];
    let wafflesPrice = wafflesCount * prices["waffle"];
    let pancakesPrice = pancakesCount * prices["pancake"]; 
    let totalDishesSum = cakesPrice + wafflesPrice + pancakesPrice;

    let total = daysCountCampaignTakesPlace * totalDishesSum * confectionersCount 
    let amountForExpenses = 1 / 8 * total;
    let charityLeft = total - amountForExpenses;

    console.log(charityLeft);
}