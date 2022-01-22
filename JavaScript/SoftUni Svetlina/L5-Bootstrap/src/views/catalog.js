import { html } from '../lib.js';

const itmCard = (img, title, id, description) => html`
<div class="card" style="width: 18rem;">
  <img class="card-img-top" src="/assets/img/nature/${img}" alt="Card image cap">
  <div class="card-body">
    <h5 class="card-title">${title}</h5>
    <p class="card-text">${description}</p>
    <a href="/details/${id}" class="btn btn-primary">Details</a>
  </div>
</div>`;

const catalogTmp = () => html`
<div class="container">
    <div class="row">
        <div class="col-sm">
            ${itmCard('nat1.jpg', 'Nature Park 1', '1', 'This is a great park!')}
        </div>
        <div class="col-sm">
            ${itmCard('nat2.jpg', 'Nature Park 2', '2', 'This is a wonderful park!')}
        </div>
        <div class="col-sm">
            ${itmCard('nat3.jpg', 'Nature Park 3', '3', 'This is a beautiful park!')}
        </div>
    </div>

    <div class="row">
        <div class="col-sm">
            ${itmCard('nat4.jpg', 'Nature Park 4', '4', 'This is a breathtaking park!')}
        </div>
        <div class="col-sm">
            ${itmCard('nat5.jpg', 'Nature Park 5','5', 'This is a nice park!')}
        </div>
        <div class="col-sm">
            ${itmCard('nat6.jpg', 'Nature Park 6', '6', 'This is a cool park!')}
        </div>
    </div>
</div>`;

export function catalogPage(ctx) {
    ctx.render(catalogTmp())
}

