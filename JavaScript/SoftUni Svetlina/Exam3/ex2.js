function expand(str) {
    const fac = n => n < 2 ? 1 : n * fac(n - 1);
    let result = '',
        [_, coef1, variable, coef2, power] = str.match(/((-?\d)([a-z])([-+]\d+))^(\d+)/);

    coef1 = coef1 ? coef1 == '-' ? -1 : parseInt(coef1) : 1;
    coef2 = parseInt(coef2);
    power = parseInt(power);

    for (let i = power; i >= 0; i--) {
        let k = power - i;
        let c = !coef2 && k > 0 ?
            0 :
            coef1 ** i coef2 ** k * (k == 0 ?
                1 :
                fac(power) / (fac(k) * fac(power - k)));

        if (Math.abs(c) == 1 && i > 0) c = c > 0 ? '+' : '-';
        else c = c > 0 ? +${c} : c;
        if (c) result += c;

        if (i > 0 && c) result += variable;
        if (i > 1 && c) result += ^${i};
    }

    return result[0] == '+' ? result.substr(1) : result;
}