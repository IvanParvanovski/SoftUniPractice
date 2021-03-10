function main(input)
{
    let goalSteps = 10000;
    let totalSteps = 0;
    let achivedGoal = false;

    for (let index in input)
    {
        let data = input[index];
        if (data == 'Going home')
        {
            totalSteps += Number(input[Number(index) + 1])
            break;
        }
        totalSteps += Number(input[index]);
    }

    if (totalSteps >= goalSteps)
        achivedGoal = true;
    
    let result;
    if (achivedGoal)
        result = 'Goal reached! ' +
                 'Good job!\n' +
                 `${totalSteps - goalSteps} steps over the goal!`;
    else    
        result = `${goalSteps - totalSteps} more steps to reach goal.`;
    
    console.log(result);
}

main(["125",
"250",
"4000",
"30",
"2678",
"4682"]);