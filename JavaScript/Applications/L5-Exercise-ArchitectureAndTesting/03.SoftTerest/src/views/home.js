const section = document.getElementById('homePage');
section.remove();
section.querySelector('#getStartedLink').addEventListener('click', (ev) => {
    ev.preventDefault();

    ctx.goTo('catalog');
});

let ctx = null;

export async function showHomePage(ctxTargex) {
    ctx = ctxTargex;
    ctx.showSection(section);
}
