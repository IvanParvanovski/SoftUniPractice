function areaOfCountry(country, area) {
    return `${country} is ${(area / 1489400).toFixed(2)}% of the total world's landmass`;
}

console.log(areaOfCountry('Russia', 17098242));

console.log(areaOfCountry('USA', 9372610));

console.log(areaOfCountry('Iran', 1648195));
