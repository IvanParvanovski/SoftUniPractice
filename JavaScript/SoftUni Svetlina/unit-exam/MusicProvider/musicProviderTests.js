const { expect } = require("chai");
const provider = require("../MusicProvider/musicProvider");


describe("Music Provider Tests", () => {
    it('returns undefined', () => {
        expect(provider(
            ['Imagine', 'One', 'Hey Jude', 'Billie Jean'], 
            ['Hey Jude'], 'Respect'
        )).to.be.undefined;
    });

    it('returns played songs', () => {
        expect(provider(
            ['Imagine', 'One', 'Hey Jude', 'Billie Jean', 'Respect'], 
            ['Hey Jude'], 'Respect'
        )).to.equal('Played songs: Hey Jude, Respect');
    })

    it('returns play on repeat', () => {
        expect(provider(
            ['Imagine', 'One', 'Hey Jude', 'Respect', 'Billie Jean'], 
            ['Hey Jude', 'Respect'], 'Respect'
        )).to.equal('Play On Repeat Respect');
    })
});
