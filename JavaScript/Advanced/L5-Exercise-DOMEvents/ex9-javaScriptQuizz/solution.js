function solve() {
	const correctAnswersList = [
		'onclick',
		'JSON.stringify()',
		'A programming API for HTML and XML documents',
	];

	let correctAnswers = 0;

	let sections = [...document.querySelectorAll('#quizzie section')];
	[...document.querySelectorAll('#quizzie .quiz-answer')].forEach((a) => {
		a.addEventListener('click', onClick);
	});
	
	function onClick(event) {
		const currentSection = sections.shift();

		const listItem = event.currentTarget;
		const answer = listItem.firstElementChild.firstElementChild.textContent;
		
		if (correctAnswersList.includes(answer)) {
			correctAnswers += 1;
		}
		
		currentSection.style.display = 'none';
		if (sections.length != 0) {
			sections[0].style.display = 'block';
		} else {
			const resultListElement = document.querySelector('#quizzie #results');
			resultListElement.style.display = 'block';

			const resultHeading = resultListElement.querySelector('.results-inner h1');

			let resultMessage;
			if (correctAnswers == correctAnswersList.length) {
				resultMessage = 'You are recognized as top JavaScript fan!';
			} else {
				resultMessage = `You have ${correctAnswers} right answers`;
			}

			resultHeading.textContent = resultMessage;
		}
	}
}
