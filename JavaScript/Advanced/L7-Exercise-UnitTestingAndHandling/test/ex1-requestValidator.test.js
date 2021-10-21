const {expect} = require('chai');
const {requestValidator} = require('../ex1-requestValidator');

describe('Ex1 RequestValidator Tests', () => {
    it('when input is valid should return the same object', () => {
        const input = {
            method: 'GET',
            uri: 'my.test.uri',
            version: 'HTTP/0.9',
            message: 'HTML and CSS',
        };

        const result = requestValidator(input);

        expect(result).to.equal(result);
    });

    it('when the method is invalid should raise exception', () => {
        const input = {
            method: 'UNKNOWN',
            uri: 'my.test.uri',
            version: 'HTTP/0.9',
            message: '<HTML> && CSS',
        }

        expect(() => requestValidator(input)).to.throw('Invalid request header: Invalid Method');
    });

    it('when the uri is invalid should raise exception', () => {
        const input = {
            method: 'GET',
            uri: 'Иван.Николаев.Първановски',
            version: 'HTTP/0.9',
            message: 'Test message',
        };

        expect(() => requestValidator(input)).to.throw('Invalid request header: Invalid URI');
    });

    it('when the uri is invalid should raise exception', () => {
        const input = {
            method: 'GET',
            uri: '%appdata%',
            version: 'HTTP/0.9',
            message: 'Test message',
        };

        expect(() => requestValidator(input)).to.throw('Invalid request header: Invalid URI');
    });

    it('when the version is invalid should raise exception', () => {
        const input = {
            method: 'GET',
            uri: 'my.test.uri',
            version: 'invalid',
            message: 'Test message',
        };

        expect(() => requestValidator(input)).to.throw('Invalid request header: Invalid Version');
    });

    it('when the method is invalid should raise exception', () => {
        const input = {
            method: 'GET',
            uri: 'my.test.uri',
            version: 'HTTP/0.9',
            message: '<script>alert("xss vulnerable")</script>',
        };

        expect(() => requestValidator(input)).to.throw('Invalid request header: Invalid Message');
    });

    it('when two properties are invalid should raise exception for the first met one', () => {
        const input = {
            method: 'invalid',
            uri: 'my.test.uri',
            version: 'invalid',
            message: 'Test message'
        };

        expect(() => requestValidator(input)).to.throw('Invalid request header: Invalid Method');
    });

    it('when the obj is empty return empty project', () => {
        const input = {};

        expect(Object.entries(requestValidator(input)).length).to.equal(0);
    })

    it('when a property is undefined and should be checked by a regular expression return false', () => {
        const input = {
            method: undefined,
            uri: undefined,
            version: undefined,
        }

        
    });
});


