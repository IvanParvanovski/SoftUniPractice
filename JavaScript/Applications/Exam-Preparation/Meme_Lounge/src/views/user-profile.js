import { getProfileMemes } from '../api/data.js';
import { html } from '../lib.js';
import { getUserData } from '../util.js';

// Profile Page ( Only for logged users )
const userMeme = (meme) => html`
<div class="user-meme">
    <p class="user-meme-title">${meme.title}</p>
    <img class="userProfileImage" alt="meme-img" src="${meme.imageUrl}">
    <a class="button" href="/details/${meme._id}">Details</a>
</div>`;

const userProfileTmp = (profile, memes) => html`
<section id="user-profile-page" class="user-profile">
    <article class="user-info">
        <img id="user-avatar-url" alt="user-profile" src="/images/female.png">
        <div class="user-content">
            <p>Username: ${profile.username}</p>
            <p>Email: ${profile.email}</p>
            <p>My memes count: ${memes.length}</p>
        </div>
    </article>
    <h1 id="user-listings-title">User Memes</h1>
    <div class="user-meme-listings">
        <!-- Display : All created memes by this user (If any) --> 
        <!-- Display : If user doesn't have own memes  --> 
    
        ${memes.length > 0 ? memes.map(userMeme) : html`<p class="no-memes">No memes in database.</p>`}
    </div>
</section>`;

export async function userProfilePage(ctx) {
    const profile = getUserData();
    const memes = await getProfileMemes(profile.id);

    ctx.render(userProfileTmp(profile, memes));
}

