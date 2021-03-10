function main(input)
{
    let floors = Number(input[0]);
    let rooms = Number(input[1]);
    for (let floor = floors; floor > 0; floor--)
    {
        let preposition;
        if (floor == floors)
            preposition = 'L';
        else if (floor % 2 == 0)
            preposition = 'O';
        else
            preposition = 'A';

        let result = '';
        for (let room = 0; room < rooms; room++)
            result += `${preposition}${floor}${room} `;
        console.log(result);
    }
}
main([6, 4])