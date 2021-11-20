const { chromium } = require('playwright-chromium');
const { expect } = require('chai');

let browser, page;

describe('E2E Tests', async function () {
    this.timeout(60000);

    before(async () => { browser = await chromium.launch({ headless: false, slowMo: 200}); });
    after(async () => { await browser.close() });
    beforeEach(async () => { page = await browser.newPage(); });
    afterEach(async () => { await page.close(); });

    it('initial load', async () => {
        await page.goto('http://localhost:5500/01.%20Accordion/');
        await page.waitForSelector('.accordion');

        const content = await page.textContent('#main');

        expect(content).to.contains('Scalable Vector Graphics');
        expect(content).to.contains('Open standard');
        expect(content).to.contains('Unix');
        expect(content).to.contains('ALGOL');
    });

    it('More button works', async () => {
        await page.goto('http://localhost:5500/01.%20Accordion/');
        await page.waitForSelector('.accordion');

        await page.click('text=More');
        await page.waitForResponse(/articles\/details/i);
        
        const visible = await page.isVisible('.accordion p');
        
        expect(visible).to.be.true;
    });

    it('Less button works', async () => {
        await page.goto('http://localhost:5500/01.%20Accordion/');
        await page.waitForSelector('.accordion');

        await page.click('text=More');
        await page.waitForResponse(/articles\/details/i);
        await page.waitForSelector('.accordion p', { state: 'visible' });
        
        await page.click('text=Less');
        
        const visible = await page.isVisible('.accordion p');

        expect(visible).to.be.false;
    });

    it.only('form input', async () => {
        await page.goto('http://localhost:5500/01.%20Accordion/');

        await page.fill('[name="email"]', 'Peter');
        await page.waitForTimeout(6000);
    });

});

