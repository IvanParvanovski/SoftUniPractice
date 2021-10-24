function notify(message) {
	const notificationElement = document.getElementById('notification');
	notificationElement.style.display = 'block';
	notificationElement.textContent = message;
	notificationElement.addEventListener('click', onClick);

	function onClick(event) {
		event.target.style.display = 'none';
	}
}