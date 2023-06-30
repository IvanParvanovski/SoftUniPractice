let footwear = {
    generateOrder: function(obj) {

        if (!obj.orderedShoes) {
            throw new Error('You must order at least one pair of shoes.');
        } else {
            let result = `Your order contains ${obj.orderedShoes}`
            if (obj.orderedLaces) {
                result += ` and ${obj.orderedLaces}.`
            }
            return result;
        }
    },

    orderStatus: function(finalAmount, statusOfOrder) {
        if (statusOfOrder === 'New') {
            finalAmount -= finalAmount * 0.1;

            return finalAmount;
        } else if (statusOfOrder === 'Delivery') {

            return finalAmount;
        }
    }
}

module.exports = footwear;