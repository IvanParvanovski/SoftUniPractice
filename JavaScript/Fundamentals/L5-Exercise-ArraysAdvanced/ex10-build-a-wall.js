function wallConstruction(wallSections) {
    let cubicYardsForOneFoot = 195;
    let totalConcrete = 0;
    let yardConcretePrice = 1900;
    let concreteDayPlan = [];

    while (wallSections.length > 0) {
        let daylyConcrete = 0;

        for (let i = wallSections.length - 1; i >= 0; i--) {
            if (wallSections[i] == 30) {
                wallSections.splice(i, 1);
            } else {
                daylyConcrete += cubicYardsForOneFoot;
                wallSections[i]++;
            }
        }
        
        totalConcrete += daylyConcrete;
        concreteDayPlan.push(daylyConcrete);
    }
    concreteDayPlan.pop();
    console.log(concreteDayPlan.join(', '));
    console.log(totalConcrete * yardConcretePrice + ' pesos');
}

wallConstruction([17, 22, 17, 19, 17]);