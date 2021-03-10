function main(input) 
{
    let strawberriesPrice = Number(input[0]);
    let rastberriesPrice = 50 / 100 * strawberriesPrice;
    let orangesPrice = 60 / 100 * rastberriesPrice
    let bananasPrice = 20 / 100 * rastberriesPrice;

    let strawberriesQuatityKilos = Number(input[4]);
    let raspberriesQuatityKilos = Number(input[3]);
    let orangesQuatityKilos = Number(input[2]);
    let bananasQuatityKilos = Number(input[1]);

    let neededSum = strawberriesPrice * strawberriesQuatityKilos +
                    rastberriesPrice * raspberriesQuatityKilos +
                    orangesPrice * orangesQuatityKilos +
                    bananasPrice * bananasQuatityKilos;
    
    console.log(neededSum);
}
