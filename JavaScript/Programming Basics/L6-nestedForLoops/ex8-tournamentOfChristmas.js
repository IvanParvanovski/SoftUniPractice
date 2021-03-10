// function main(input)
// {
//     let tourfilmntDays = Number(input[0]);

//     let totalMoney = 0;
//     let wonDays = 0;
//     let lostDays = 0;

//     let index = 1;
//     for (let day = 0; day < tourfilmntDays; day++)
//     {
//         let moneyPerDay = 0;
//         let wonGames = 0;
//         let lostGames = 0;
//         while (true)
//         {
//             if (index >= input.length)
//                 break;

//             data = input[index];
//             if (data == 'Finish')
//                 break;
            
//             let sport = data;
//             index++;
    
//             let status = input[index];
//             index++;
    
//             if (status == 'win')
//             {
//                 moneyPerDay += 20;
//                 wonGames++;
//             }
//             else
//                 lostGames++;            
//         }

//         totalMoney += moneyPerDay;
//         if (wonGames > lostGames)
//         {
//             totalMoney += 0.1 * moneyPerDay;
//             wonDays++;
//         }
//         else
//             lostDays++;
            
//         index++;
//     }
//     let result;
//     if (wonDays > lostDays)
//     {
//         result = 'won'
//         totalMoney += 0.2 * totalMoney;
//     }
//     else 
//     {
//         result = 'lost';
//     }
//     console.log(`You ${result} the tourfilmnt! Total raised money: ${totalMoney.toFixed(2)}`);        
// }

function main(input)
{
    let index = 0;


    let totalTickets = 0;
    let studentTickets = 0;
    let standardTickets = 0;
    let kidTickets = 0;

    while (true)
    {
        let data = input[index];
        if (data == 'Finish')
            break;

        let film = data;
        index++;
        
        let roomSeats = Number(input[index]);
        let totalStudents = 0;
        while (true)
        {
            if (roomSeats == totalStudents)
                break;
            
            index++;
            let type = input[index];
            if (type == 'End')
                break; 
            
            switch (type)
            {
                case 'standard':
                    standardTickets++;
                    break;
                case 'student':
                    studentTickets++;
                    break;
                case 'kid':
                    kidTickets++;
                    break;
            }
            totalStudents++;
            totalTickets++;   
        }

        console.log(`${film} - ${(totalStudents / roomSeats * 100).toFixed(2)}% full.`);
        index++;
    }
    console.log(`Total tickets: ${totalTickets}`);
    console.log(`${(studentTickets / totalTickets * 100).toFixed(2)}% student tickets.`);
    console.log(`${(standardTickets / totalTickets * 100).toFixed(2)}% standard tickets.`);
    console.log(`${(kidTickets / totalTickets * 100).toFixed(2)}% kids tickets.`);
}

main((["Taxi",
"10",
"standard",
"kid",
"student",
"student",
"standard",
"standard",
"End",
"Scary Movie",
"6",
"student",
"student",
"student",
"student",
"student",
"student",
"Finish"]));
// main((["2",
// "volleyball",
// "win",
// "football",
// "lose",
// "basketball",
// "win",
// "Finish",
// "golf",
// "win",
// "tennis",
// "win",
// "badminton",
// "win",
// "Finish"])
// );