function main(input)
{
    let salary = Number(input[0]);
    let averageGrade = Number(input[1]);
    let minimumSalaray = Number(input[2]);

    let socialScholarshipValue = 0; 
    let excellentScholarsipValue = 0;
    let result;

    let socialScholarship = false;
    let excellentScholarship = false;

    if (salary <= minimumSalaray && averageGrade > 4.5)
    {
        socialScholarship = true;
        socialScholarshipValue = Math.floor(0.35 * minimumSalaray)
    }
    
    if (averageGrade >= 5.5)
    {
        excellentScholarship = true;
        excellentScholarsipValue = Math.floor(25 * averageGrade)
    }
    
    if (!(excellentScholarship || socialScholarship))
        result = 'You cannot get a scholarship!';
    else if (excellentScholarsipValue > socialScholarshipValue)
        result = `You get a scholarship for excellent results ${excellentScholarsipValue} BGN`;
    else
        result = `You get a Social scholarship ${socialScholarshipValue} BGN`;

    console.log(result);
}

main([1020, 5.50, 450]);