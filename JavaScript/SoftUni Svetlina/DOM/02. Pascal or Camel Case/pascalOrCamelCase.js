function solve() {
  const words = document
    .getElementById('text')
    .value
    .toLowerCase()
    .split(' ');
  
  const namingConvention = document.getElementById('naming-convention').value;
  const result = document.getElementById('result');

  if (namingConvention == 'Pascal Case') {
    result.textContent = words.map(
      (x) => x[0].toUpperCase() + x.substring(1, x.length)
    ).join('');

  } else if (namingConvention == 'Camel Case') {
    result.textContent = words.map(
      (x, i) => {
        let temp = x;

        if (i != 0) { 
          temp = x[0].toUpperCase() + x.substring(1, x.length)
        }

        return temp;
      }).join('');
  } else {
    result.textContent = 'Error!';
  }
}
