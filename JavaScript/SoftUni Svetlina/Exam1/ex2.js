function areaOfCountry(country, area) {
    console.log(`${country} is ${(area / 148940000 * 100).toFixed(2)}% of the total world's landmass`);
}

areaOfCountry('Russia', 17098242);
areaOfCountry('USA', 9372610);
areaOfCountry('Iran', 1648195);
