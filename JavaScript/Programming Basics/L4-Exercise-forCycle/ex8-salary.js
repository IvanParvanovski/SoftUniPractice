function main(input)
{
    let tabsCount = Number(input[0]);
    let salary = Number(input[1]);

    for (let i = 2; i < tabsCount + 2; i++)
    {
        if (salary <= 0) 
        {
            console.log('You have lost your salary.');
            return;
        }
        
        let tab = input[i];
        switch (tab)
        {
            case 'Facebook':
                salary -= 150;
                break;
            case 'Instagram':
                salary -= 100;
                break;
            case 'Reddit':
                salary -= 50;
                break;
        }
    }
    console.log(salary);
}

main(["3",
"500",
"Github.com",
"Stackoverflow.com",
"softuni.bg"]);