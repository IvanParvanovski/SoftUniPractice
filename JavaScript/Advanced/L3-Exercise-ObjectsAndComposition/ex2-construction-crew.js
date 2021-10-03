function constructionCrew(worker) {
    let neededWater = 0.1 * worker.weight * worker.experience;
    
    if (worker.dizziness) {
        worker.levelOfHydrated += neededWater;
        worker.dizziness = false;
    }

    return worker;
}

console.log(constructionCrew({ 
    weight: 80,
    experience: 1,
    levelOfHydrated: 0,
    dizziness: true 
}));
