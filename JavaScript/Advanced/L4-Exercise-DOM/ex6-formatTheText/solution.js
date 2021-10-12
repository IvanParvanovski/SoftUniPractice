function solve() {
  const text = document.getElementById('input').value;
  let resultElement = document.getElementById('output');

  const sentences = text.split('.').filter((x) => x != '');
  const result = [];
  let currentParagraph = [];

  for (let i = 0; i < sentences.length; i++) {
    currentParagraph.push(sentences[i]);

    if ((i + 1) % 3 == 0) {
      result.push(`<p>${currentParagraph.join('.')}.</p>`);
      currentParagraph = [];
    }
  }

  if (currentParagraph.length > 0 && currentParagraph.length < 3) {
    result.push(`<p>${currentParagraph.join('.')}.</p>`);
    currentParagraph = [];
  }

  console.log(result);
  resultElement.innerHTML = result.join('');
}

// function solve() {
//   const text = document.getElementById('input').value;
//   let resultElement = document.getElementById('output');
//   const sentences = text.split('.').filter((x) => x != '');

//   for (let i = 0; i < sentences.length; i += 3) {
//     let arr = [];
    
//     for (let y = 0; y < 3; y++) {
//       if (sentences[i + y]) {
//         arr.push(sentences[i + y]);
//       }
//     } 

//     let paragraph = arr.join('. ') + '.';
//     resultElement.innerHTML = `<p>${paragraph}</p>`;
//   }
// }