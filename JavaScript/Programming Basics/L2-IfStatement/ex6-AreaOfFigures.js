function main(input)
{
    let shape = input[0];
    let side = Number(input[1]);
    let result;

    if (shape == 'square')
    {
        result = side * side;
    }

    else if (shape == 'circle')
    {
        result = Math.pow(side, 2) * Math.PI;
    }

    else if (shape == 'rectangle')
    {
        let width = Number(input[2]);
        result = width * side
    }

    else if (shape == 'triangle')
    {
        let heigth = Number(input[2]);
        result = side * heigth / 2
    }

    console.log(result.toFixed(3));
}