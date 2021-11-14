import { showSection } from './dom.js';

const homeSection = document.getElementById('homeSection');
homeSection.remove();

export function showHomePage() {
    showSection(homeSection);
}

