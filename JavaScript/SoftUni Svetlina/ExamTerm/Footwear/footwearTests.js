const expect = require('chai').expect;
const footwear = require('./footwear');


describe("Tests", () => {
    describe("Footwear test", () => {
        it("test generateOrder, should return positive number when order is positive", function() {
            expect(footwear.generateOrder(
                { orderedShoes: 1 })
            ).to.equal("Your order contains 1");
        });

        it("test generateOrder, should throw an error when empty", function() {
            expect(() => footwear.generateOrder({})).to.throw(Error, "You must order at least one pair of shoes.");
        });

        it("test generateOrder, should return positive numbers when laces and shoes are positive", function() {
            expect(footwear.generateOrder({ 
                orderedShoes: 1, 
                orderedLaces: 1 
            })).to.equal("Your order contains 1 and 1.");
        });

        it("test orderStatus, should not make a discount when different from new", function() {
            expect(footwear.orderStatus(100, "Delivery")).to.equal(100);
        });

        it("test orderStatus, should make a discount when new", function() {
            expect(footwear.orderStatus(100, "New")).to.equal(90);
        });

        it("test orderStatus, should not make a discount when status is random", function () {
            expect(footwear.orderStatus(1, 'Random')).to.equal(undefined);
        });
    });

});