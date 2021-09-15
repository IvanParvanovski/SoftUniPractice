function getDaysInMonth(month, year) {
    let date = new Date(year, month, 0);

    console.log(date.getDate());
}

getDaysInMonth(1, 2012);
