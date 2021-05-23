function calculateNeededMaterials(base, increment) {
    let step = 1;
    
    let materials = {
        'stone': 0,
        'marble': 0,
        'lapis': 0,
        'gold': 0,
    };

    for (let i = base; i >= 0; i -= 2) {
       
        let insideMaterial = 'stone';
        let outsideMaterial = 'marble';

        
        let fullArea = i * i;
        let outsideArea = i * 4;
        let insideArea = fullArea - outsideArea;

        if (step % 5 == 0) {
            outsideMaterial = 'lapis';
        }

        if (i - 2 <= 0) {
            outsideMaterial = 'gold';
        }

        materials[insideMaterial] += insideArea * increment;
        materials[outsideMaterial] += outsideArea * increment;
        step++;
    }
    console.log(materials);
}

calculateNeededMaterials(11, 1);
