function pyramid(base, increment) {
    let step = 1;
    let neededMaterials = {
        'gold': 0,
        'lapis': 0,
        'marble': 0,
        'stone': 0,
    }

    for (let i = base; i > 0; i -= 2) {
        let internalMaterial = 'stone';
        let externalMaterial = 'marble';

        if (step % 5 == 0) {
            externalMaterial = 'lapis';
        }

        let fullArea = i * i;
        let externalArea = i + 2 * (i - 1) + i - 2;
        let internalArea = fullArea - externalArea;

        if (i - 2 <= 0) {
            externalMaterial = 'gold';
            internalMaterial = 'gold';
        }

        neededMaterials[externalMaterial] += externalArea * increment;
        neededMaterials[internalMaterial] += internalArea * increment;
        step++;
    }
    console.log(`Stone required: ${Math.ceil(neededMaterials['stone'])}`);
    console.log(`Marble required: ${Math.ceil(neededMaterials['marble'])}`);
    console.log(`Lapis Lazuli required: ${Math.ceil(neededMaterials['lapis'])}`);
    console.log(`Gold required: ${Math.ceil(neededMaterials['gold'])}`);
    console.log(`Final pyramid height: ${Math.floor(--step * increment)}`);
}

// pyramid(11, 1);
// pyramid(11, 0.75);
// pyramid(23, 0.5);
pyramid(12, 1);
