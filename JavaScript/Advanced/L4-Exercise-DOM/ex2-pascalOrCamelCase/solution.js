function solve() {
  const text = document.getElementById('text').value;
  const convention = document.getElementById('naming-convention').value;
  const resultElement = document.getElementById('result');
  const textTokens = text.split(' ');

  let result = [];

  if (convention == 'Camel Case') {
    for (let i = 0; i < textTokens.length; i++) {
      const currentToken = textTokens[i].toLowerCase();

      if (i == 0) {
        result.push(currentToken);
      } else {
        result.push(currentToken[0].toUpperCase() + currentToken.slice(1));
      }
    }
  } else if (convention == 'Pascal Case') {
    for (const token of textTokens) {
      const tokenToLower = token.toLowerCase();
      result.push(tokenToLower[0].toUpperCase() + tokenToLower.slice(1));
    }
  } else {
    result.push('Error!');
  }

  resultElement.textContent = result.join('');
}
