function main(input)
{
    let name = input[0];
    let gradesSum = 0;

    let failedTimes = 0;
    let failed = false;
    let failedGrade = 0;

    for (let i = 1; i < input.length; i++)
    {
        let grade = Number(input[i]);

        if (grade < 4)
            failedTimes++;

        if (failedTimes > 1)
        {
            failed = true;
            failedGrade = i - 1;
            break;
        }

        gradesSum += grade;
    }

    let result;
    if (failed)
        result = `${name} has been excluded at ${failedGrade} grade`;
    else
        result = `${name} graduated. Average grade: ${(gradesSum / 12).toFixed(2)}`;
    
    console.log(result);
}

main(["Mimi", 
"5",
"6",
"5",
"6",
"5",
"6",
"6",
"2",
"3"]);
