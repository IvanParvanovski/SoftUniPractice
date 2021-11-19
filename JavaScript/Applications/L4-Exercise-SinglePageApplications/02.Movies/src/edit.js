import { showView } from "./dom.js";

const editSection = document.getElementById('edit-movie');
editSection.remove();

export function showEdit() {
    showView(editSection);
}
