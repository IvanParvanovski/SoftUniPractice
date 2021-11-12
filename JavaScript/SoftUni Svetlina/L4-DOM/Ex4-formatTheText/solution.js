function solve() {
    function createParagraph(collection, start, end) {
        return `<p>${collection.slice(start, end).join('.')}.</p>`;
    }

    const sentences = document.getElementById('input').textContent.split('.').filter((x) => x != '');
    const paragraphs = [];
    let sl = sentences.length;

    for (let i = 0; i < sl; i++) {
        if ((i + 1) % 3 == 0) {
            paragraphs.push(createParagraph(sentences, i - 2, i + 1));
        }
    }

    while (sl % 3 != 0) { sl--; }
    
    paragraphs.push(createParagraph(sentences, sl, sentences.length));
    document.getElementById('output').innerHTML = paragraphs.join('');
}
