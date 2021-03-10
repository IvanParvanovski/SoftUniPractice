function main(input)
{
    let unsatisfiedGrades = Number(input.shift());
    let marinUnsatisfiedGrades = 0;

    let unsatisfied = false;
    let marinTotalScore = 0;
    let problemsQuantity = 0;
    let lastProblem = '';

    for (let i = 0; i < input.length; i += 2)
    {
        let word = input[i];
        if (word == 'Enough')
            break;
        
        let grade = Number(input[i + 1]);
        if (grade <= 4)
            marinUnsatisfiedGrades++;
    
        if (marinUnsatisfiedGrades >= unsatisfiedGrades)
        {
            unsatisfied = true;
            break;
        }

        marinTotalScore += grade;
        problemsQuantity++;
        lastProblem = word;
    }

    let result;
    if (unsatisfied)
        result = `You need a break, ${marinUnsatisfiedGrades} poor grades.`;
    else
        result = `Average score: ${(marinTotalScore / problemsQuantity).toFixed(2)}\n` +
                 `Number of problems: ${problemsQuantity}\n` +
                 `Last problem: ${lastProblem}`;
    
    console.log(result);
}

main(["2",
"Income",
"3",
"Game Info",
"6",
"Best Player",
"4"]);
