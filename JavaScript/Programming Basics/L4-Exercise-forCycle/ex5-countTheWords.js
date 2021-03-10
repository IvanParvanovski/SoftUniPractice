function main(input)
{   
    let result;
    let n = input[0].split(' ').length;
    if (n > 10)
        result = `The message is too long to be send! Has ${n} words.`
    else
        result = 'The message was send successfully!';
    console.log(result);
}

main(["This message has exactly eleven words. One more as it's allowed!"])