function main(input)
{

    let total = 0;
    let students = 0;
    let kids = 0;
    let standard = 0;

    for (let index = 0; index < input.length; index++)
    {
        let data;
        data = input[index];
        if (data == 'Finish')
            break;

        let film = data;
        index++;

        let roomSeats = Number(input[index]);
        let totalStudents = 0;
        while (true)
        {
            if (totalStudents == roomSeats)
                break;

            index++;
            data = input[index];
            if (data == 'End')
                break;
            
            let ticketType = data;
            switch (ticketType)
            {
                case 'kid':
                    kids++;
                    break;
                case 'student':
                    students++;
                    break;
                case 'standard':
                    standard++;
                    break;
            }

            totalStudents++;
            total++;
        }
        console.log(`${film} - ${(totalStudents / roomSeats * 100).toFixed(2)}% full.`);
    }
    console.log(`Total tickets: ${total}`);
    console.log(`${(students / total * 100).toFixed(2)}% student tickets.`);
    console.log(`${(standard / total * 100).toFixed(2)}% standard tickets.`);
    console.log(`${(kids / total * 100).toFixed(2)}% kids tickets.`);
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