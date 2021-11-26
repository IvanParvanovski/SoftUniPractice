import { showSection } from './dom.js';

const aboutSection = document.getElementById('aboutSection');
aboutSection.remove();

export function showAboutPage() {
    showSection(aboutSection);
}
