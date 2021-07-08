function gladiatorInventory(input) {
    function removeItem(array, item) {
        if (array.includes(item)) {
            array.splice(array.indexOf(item), 1);
        }
    }

    let inventory = input.shift().split(' ');
    while (input.length > 0) {
        let rawCommand = input.shift().split(' ');
        let command = rawCommand[0];
        let item = rawCommand[1];

        switch (command) {
            case 'Buy':
                if (!inventory.includes(item)) {
                    inventory.push(item);
                }
                break;

            case 'Trash':
                removeItem(inventory, item);
                break;
            
            case 'Repair':
                removeItem(inventory, item);
                inventory.push(item);
                break;
            
            case 'Upgrade':
                let itemInfo = item.split('-');
                let itemName = itemInfo[0];
                let itemUpgrade = itemInfo[1];

                if (inventory.includes(itemName)) {
                    let itemIndex = inventory.indexOf(itemName);
                    inventory.splice(itemIndex + 1, 0, `${inventory[itemIndex]}:${itemUpgrade}`);
                }
                break;
        }
    }

    console.log(inventory.join(' '));
}

// gladiatorInventory(['SWORD Shield Spear',
// 'Buy Bag',
// 'Trash Shield',
// 'Repair Spear',
// 'Upgrade SWORD-Steel']
// );

gladiatorInventory(['SWORD Shield Spear',
'Trash Bow',
'Repair Shield',
'Upgrade Helmet-V']
);