function main(input)
{
    let product = input[0];
    let town = input[1];
    let quantity = Number(input[2]);
    let market = {
        'coffee': {
            'Sofia': 0.50,
            'Plovdiv': 0.40,
            'Varna': 0.45,
        },

        'water': {
            'Sofia': 0.80,
            'Plovdiv': 0.70,
            'Varna': 0.70,
        },

        'beer': {
            'Sofia': 1.20,
            'Plovdiv': 1.15,
            'Varna': 1.10,
        },

        'sweets': {
            'Sofia': 1.45,
            'Plovdiv': 1.30,
            'Varna': 1.35,
        },

        'peanuts': {
            'Sofia': 1.60,
            'Plovdiv': 1.50,
            'Varna': 1.55,
        },
    };

    console.log(market[product][town] * quantity);
}

main(["coffee", "Varna", "2"]);

main(["peanuts", "Plovdiv", "1"]);

main(["beer", "Sofia", "6"]);

main(["water", "Plovdiv", "3"]);

main(["sweets", "Sofia", "2.23"]);
