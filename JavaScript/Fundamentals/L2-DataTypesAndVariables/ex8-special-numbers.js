function specialNumebers(num) {
    for (let i = 1; i <= num; i++) {
        let numAsString = i.toString();
        let numSum = 0;

        for (let j = 0; j < numAsString.length; j++) {
            numSum += Number(numAsString[j]);
        }
        
        let expression = numSum == 5 || numSum == 7 || numSum == 11;
        console.log(expression ? `${i} -> True` : `${i} -> False`);
    }

}

specialNumebers(15);