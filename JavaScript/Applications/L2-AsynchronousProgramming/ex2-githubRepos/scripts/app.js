function loadRepos() {
	const username = document.getElementById('username').value;
	const url = `https://api.github.com/users/${username}/repos`;
	const listElement = document.getElementById('repos');

	function clearList(listElement) {
		const listItems = listElement.children;
		
		for (let i = listItems.length - 1; i >= 0; i--) {
			const currentElement = listItems[i];
			listElement.removeChild(currentElement);
		}
	}

	function addItem(itemData, list) {
		const newItem = document.createElement('li');

		newItem.innerHTML = `<a href=${itemData.html_url}>${itemData.full_name}</a>`;
		list.appendChild(newItem);
	}

	function handleResponse(data) {
		clearList(listElement);

		for (const project of data) {
			addItem(project, listElement);
		}
	}

	function handleError(error) {
		clearList(listElement);
		console.log(error);
	}

	fetch(url)
		.then(res => {
			if (res.ok == false) {
				throw new Error(`${res.status} ${res.statusText}`);
			}

			return res.json()
		})
		.then(handleResponse)
		.catch(handleError);
}
