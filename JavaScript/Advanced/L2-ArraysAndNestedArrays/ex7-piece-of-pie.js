function pieceOfPie(
    pieFlavours,
    firstTargetPie,
    secondTargetPie) {

    let firstTargetIndex = pieFlavours.indexOf(firstTargetPie);
    let secondTargetIndex = pieFlavours.indexOf(secondTargetPie);

    return pieFlavours.slice(firstTargetIndex, secondTargetIndex + 1);
}

pieceOfPie([
    'Pumpkin Pie',
    'Key Lime Pie',
    'Cherry Pie',
    'Lemon Meringue Pie',
    'Sugar Cream Pie'],
    'Key Lime Pie',
    'Lemon Meringue Pie');
