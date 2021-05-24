function login(data) {
    let username = data.shift();   
    let password = username.split('').reverse().join('');
    
    for (let i = 0; i < 4; i++)
    {
        let currentPassword = data.shift();
        
        if (currentPassword === password) {
            console.log(`User ${username} logged in.`);
            break;
        } else {
            if (i == 3) {
                console.log(`User ${username} blocked!`);
            } else {
                console.log("Incorrect password. Try again.");
            }
        }
    }
}

login(['Acer','login','go','let me in','recA']);
login(['momo','omom']);
login(['sunny','rainy','cloudy','sunny','not sunny']);
