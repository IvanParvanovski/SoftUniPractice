import { showView } from "./dom.js";

const createSection = document.getElementById('add-movie');
createSection.remove();

export function showCreate() {
    showView(createSection);
}
