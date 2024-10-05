const { connect } = require("puppeteer-real-browser");
const fs = require("fs");
const Papa = require("papaparse");

async function test() {
    const { browser, page } = await connect({
        headless: false,
        args: [],
        customConfig: {},
        turnstile: true,
        connectOption: {},
        disableXvfb: false,
        ignoreAllFlags: false,
        // proxy:{
        //     host:'<proxy-host>',
        //     port:'<proxy-port>',
        //     username:'<proxy-username>',
        //     password:'<proxy-password>'
        // }
    });

    await page.goto('https://www.prioritytire.com/by-brand/yokohama-tires');

    // Extract data
    const data = await page.evaluate(() => {
        const products = [];
        const productElements = document.querySelectorAll('.product-info-wrapper'); // Update selector as necessary

        productElements.forEach(product => {
            const name = product.querySelector('.product-attributes')?.innerText || 'N/A';
            const price = product.querySelector('.price-box.price-final_price')?.innerText || 'N/A';
            const stock = product.querySelector('.product-stock')?.innerText || 'N/A';

            products.push({ name, price, stock });
        });

        return products;
    });

    // Convert data to CSV
    const csv = Papa.unparse(data);

    // Save CSV to file
    fs.writeFileSync('yokohama_tires.csv', csv);

    console.log('Data saved to yokohama_tires.csv');

    await browser.close();
}

test().catch(error => {
    console.error('Error:', error);
});
