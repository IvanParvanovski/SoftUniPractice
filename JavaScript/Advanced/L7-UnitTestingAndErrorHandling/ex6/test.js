const {expect} = require('chai'); 
const rgbToHexColor = require('./ex6-rgbToHex');

describe('Ex6 RgbToHex Tests', () => {
    it('returns the color red', () => {
        expect(rgbToHexColor(240, 0, 0)).to.equal('#F00000');
    });

    it('returns the color white', () => {
        expect(rgbToHexColor(255, 255, 255)).to.equal('#FFFFFF');
    });

    it('returns undefined if doubles', () => {
        expect(rgbToHexColor(0.2, 2, 2)).to.equal(undefined);
    })

    it('returns undefined when a string is given', () => {
        expect(rgbToHexColor('hi', 20, 40)).to.equal(undefined);
    });

    it('returns undefined when a number is above the range [0:255]', () => {
        expect(rgbToHexColor(256, 20, 20)).to.equal(undefined);
    });

    it('returns undefined when a number is under the range [0:255]', () => {
        expect(rgbToHexColor(-1, 20, 20)).to.equal(undefined);
    }); 

    it('returns undefined when two parameters are given', () => {
        expect(rgbToHexColor(0, 0)).to.equal(undefined);
    });
});