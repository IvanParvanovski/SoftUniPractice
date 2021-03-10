function main(input) 
{
    let length = Number(input[0]);
    let width = Number(input[1]);
    let height = Number(input[2]);
    let percent = Number(input[3]);
    
    let littersInCM = length * height * width;
    let litters = littersInCM * 0.001;
    let items = litters * percent / 100;
    console.log(litters - items);
    
}
