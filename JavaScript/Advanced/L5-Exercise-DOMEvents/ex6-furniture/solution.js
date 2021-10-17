function solve() {
	const generateButton = document.querySelector('#exercise button');
	generateButton.addEventListener('click', generateProduct);

	const buyButton = document.querySelector('#exercise button:last-of-type');
	buyButton.addEventListener('click', buyProducts);

	function generateProduct(event) {
		const properties = [
			'img',
			'name',
			'price',
			'decFactor',
			'checkbox',
		];

		const productTable = document.querySelector('.table tbody');
		
		const productTextarea = event.target.parentElement.querySelector('textarea');
		const productsInfo = JSON.parse(productTextarea.value);

		for (productInfo of productsInfo) {
			const newRow = document.createElement('tr');
			
			for (const prop of properties) {
				const newData = document.createElement('td');
				const propValue = productInfo[prop];
				let element;

				if (prop == 'img') {
					element = document.createElement('img');	
					element.src = propValue;
				} else if (prop == 'checkbox') {
					element = document.createElement('input');
					element.type = 'checkbox';
				} else {
					element = document.createElement('p');
					element.textContent = propValue;
				}

				newData.appendChild(element);
				newRow.appendChild(newData);
			}

			productTable.appendChild(newRow);
		}
	}

	function buyProducts(event) {
		const result = {
			boughtFurniture: [],
			totalPrice: 0,
			decorationFactor: 0,
		};

		const resultTextarea = document.querySelector('#exercise textarea:last-of-type');
		const rows = [...document.querySelectorAll('.table tbody tr')];
		
		const checkedRows = rows.filter((r) => {
			const cellsLength = r.cells.length;
			if (r.cells[cellsLength - 1].firstElementChild.checked) {
				return r;
			}
		});

		for (let row of checkedRows) {
			result.boughtFurniture.push(row.cells[1].firstElementChild.textContent);
			result.totalPrice += Number(row.cells[2].firstElementChild.textContent);
			result.decorationFactor += Number(row.cells[3].firstElementChild.textContent)
		}

		const resultMessage = 
			`Bought furniture: ${result.boughtFurniture.join(', ')}\n` +
			`Total price: ${result.totalPrice.toFixed(2)}\n` + 
			`Average decoration factor: ${result.decorationFactor / result.boughtFurniture.length}`;
		
		resultTextarea.value = resultMessage;
	}
}
