import { html } from '../node_modules/lit-html/lit-html.js';
import { loadCats } from '../app.js';

const catCard = (cat) => html`
<li>
    <img src="images/${cat.imageLocation}.jpg" width="250" height="250" alt="Card image cap">
    <div class="info">
        <button class="showBtn" @click=${() => toggleInfo(cat)}>${cat.display ? 'Hide' : 'Show'} status code</button>
        
        <div class="status" style="display: ${cat.display ? 'block' : 'none'}" id="${cat.id}">
            <h4>Status Code: ${cat.statusCode}</h4>
            <p>${cat.statusMessage}</p>
        </div>
    </div>
</li>`;

function toggleInfo(cat) {
    cat.display = !(cat.display);
    loadCats();
}

export default catCard;
