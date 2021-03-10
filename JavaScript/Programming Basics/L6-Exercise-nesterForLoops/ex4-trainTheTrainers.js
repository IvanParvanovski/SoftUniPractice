function main(input)
{
    let gradesCount = Number(input[0]);
    let finalGrade = 0;
    let projects = 0;

    let index = 1;
    while (true)
    {
        let data = input[index]
        if (data == 'Finish')
            break;
        
        let project = data;
        let total = 0;
        for (let gradeCounter = 1; gradeCounter <= gradesCount; gradeCounter++)
            total += Number(input[index + gradeCounter]);
        
        let averageGrade = total / gradesCount;
        console.log(`${project} - ${averageGrade.toFixed(2)}.`);
        finalGrade += averageGrade;
        projects++;
        index += gradesCount + 1;
    }
    console.log(`Student's final assessment is ${(finalGrade / projects).toFixed(2)}.`);
}

main(["3",
"Arrays",
"4.53",
"5.23",
"5.00",
"Lists",
"5.83",
"6.00",
"5.42",
"Finish"]);