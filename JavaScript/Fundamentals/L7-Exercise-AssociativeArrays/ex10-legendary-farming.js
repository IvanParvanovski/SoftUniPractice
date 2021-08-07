function legendaryFarming(materials) {
    function findLegendaryItem(legendaryItems, component) {
        return Object.entries(legendaryItems).find(x => x[1].component == component);
    }

    let neededQuantity = 250;

    let legendaryItems = {
        Shadowmourne: {
            component: 'shards',
            neededQuantity,    
        },
        Valanyr: {
            component: 'fragments',
            neededQuantity,
        },
        Dragonwrath: {
            component: 'motes',
            neededQuantity,
        },
    };

    let keyMaterials = {
        shards: 0, 
        fragments: 0,
        motes: 0
    };

    let junkMaterials = {};

    let materialsTokens = materials.split(' ');
    
    let builtItem;
    for (let i = 0; i < materialsTokens.length; i += 2) {
        let [quantity, material] = [
            Number(materialsTokens[i]),
            materialsTokens[i + 1].toLowerCase(),
        ];
        
        if (Object.keys(keyMaterials).includes(material)) {
            keyMaterials[material] += quantity;
            
            let legendaryItemBuiltByThisMaterial = findLegendaryItem(legendaryItems, material);
            let legendaryItemName = legendaryItemBuiltByThisMaterial[0]
            let neededAmountToBuilt = legendaryItemBuiltByThisMaterial[1].neededQuantity;

            if (keyMaterials[material] >= neededAmountToBuilt) {
                keyMaterials[material] -= neededAmountToBuilt;
                builtItem = legendaryItemName;
                break;
            }
        } else {
            if (!Object.keys(junkMaterials).includes(material)) {
                junkMaterials[material] = 0;
            }

            junkMaterials[material] += quantity;
        }
    }

    let sortedKeyMaterials = Object.entries(keyMaterials).sort((a, b) => {
        let aComponentName = a[0];
        let bComponentName = b[0];

        let aQuantity = a[1];
        let bQuantity = b[1];

        // Sort by quantity
        if (aQuantity < bQuantity) {
            return 1;
        } else if (aQuantity > bQuantity) {
            return -1;
        }

        // Sort by name ascending order
        return aComponentName.localeCompare(bComponentName);
    });

    let sortedJunkMaterials = Object.entries(junkMaterials).sort((a, b) => a[0].localeCompare(b[0]));
    
    console.log(`${builtItem} obtained!`);
    sortedKeyMaterials.forEach(keyMaterial => console.log(keyMaterial.join(': ')));
    sortedJunkMaterials.forEach(junkMaterial => console.log(junkMaterial.join(': ')));
}

// legendaryFarming('3 Motes 5 stones 5 Shards 6 leathers 255 fragments 7 Shards');
legendaryFarming('123 silver 6 shards 8 shards 5 motes 9 fangs 75 motes 103 MOTES 8 Shards 86 Motes 7 stones 19 silver');
