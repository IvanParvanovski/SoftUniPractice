function main(input)
{
    let minutes = Number(input[0]) * 60 + Number(input[1]);
    minutes += 15;

    let hours = Math.trunc(minutes / 60);
    minutes %= 60;

    if (hours == 24)
        hours = 0;

    let result;
    if (minutes < 10)
        result = `${hours}:0${minutes}`;
    else
        result = `${hours}:${minutes}`;
    
    console.log(result);
}
