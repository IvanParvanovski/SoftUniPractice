function createArticle() {
	function setElementValue(value, type) {
		if (value == '') {
			throw new Error('The field should have value!');
		}
	
		const newElement = document.createElement(type);
		newElement.textContent = value;
		
		return newElement;
	}

	const newArticle = document.createElement('article');
	
	const headingInput = document.getElementById('createTitle');
	const paragraphInput = document.getElementById('createContent');

	try {
		newArticle.appendChild(
			setElementValue(headingInput.value, 'h3'),
		);
	
		newArticle.appendChild(
			setElementValue(paragraphInput.value, 'p'),
		);

		headingInput.value = '';
		paragraphInput.value = '';
		document.getElementById('articles').appendChild(newArticle);
	} catch (err) {
		console.log(err);
	}
}
