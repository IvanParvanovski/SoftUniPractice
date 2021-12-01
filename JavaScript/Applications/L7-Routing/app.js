import page from '/node_modules/page/page.mjs'

function homePage(ctx, next) {
    console.log(ctx);
    console.log(next);
    main.innerHTML = '<h2>Home Page</h2><p>Welcome to our site!</p>';
}

function catalogPage() {
    main.innerHTML = [
        '<h2>Catalog</h2>',
        `<a href="catalog/${1}">`,
        '<p>Product details</p>'
    ].join();
}

function detailsPage(ctx) {
    let id = ctx.params.id;
    
    main.innerHTML = [
        `<h2>Product ${id}</h2>`,
        '<p>List of items</p>',
        '<button>Buy now</button>',
    ].join('');

    document.querySelector('button').addEventListener('click', (ev) => {
        page.redirect('/checkout');
    });
}

function checkoutPage() {
    main.innerHTML = `<h2>Card details</h2><p>Products in card</p><a href="/catalog/1"></a>`;
}

function aboutPage() {
    main.innerHTML = '<h2>About Us</h2><p>Contact: +1-555-7915</p>';
}

const main = document.querySelector('main');

page('/home', homePage);
page('/catalog', catalogPage);
page('/catalog/:id', detailsPage);
page('/about', aboutPage);
page('/checkout', checkoutPage);

page.redirect('/', '/home');
page.start();
