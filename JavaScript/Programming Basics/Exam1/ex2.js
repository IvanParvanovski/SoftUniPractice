function main(input)
{
    let planedProcesorsCount = Number(input[0]);
    let employees = Number(input[1]);
    let workingDays = Number(input[2]);

    let procesorBuildHours = 3;
    let employeeWorkingHours = 8;

    let totalHours = employees * workingDays * employeeWorkingHours;
    let totalProcesors = Math.floor(totalHours / procesorBuildHours);

    let diff = totalProcesors - planedProcesorsCount;
    
    let result;
    if (diff < 0)
        result = 'Losses'
    else
        result = 'Profit'

    console.log(`${result}: -> ${(Math.abs(diff) * 110.10).toFixed(2)} BGN`);

}

main([150, 7, 18]);