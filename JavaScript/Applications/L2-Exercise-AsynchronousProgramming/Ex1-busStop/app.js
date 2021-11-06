function getInfo() {
    const stopId = document.getElementById('stopId').value;
    const url = `http://localhost:3030/jsonstore/bus/businfo/${stopId}`;
    
    const resultElement = document.getElementById('result'); 
    const stopNameElement = resultElement.querySelector('#stopName');
    const busesElement = resultElement.querySelector('#buses');

    function handleError(error) {
        stopNameElement.textContent = 'Error';

        console.error(error);
    }

    function handleData(data) {
        stopNameElement.textContent = data.name;

        for (const busNumber in data.buses) {
            const time = data[busNumber]; 
            const newItem = document.createElement('li');
            newItem.textContent = `Bus ${busNumber} arrives in ${time} minutes`
            
            busesElement.appendChild(newItem);
        }
    }

    busesElement.replaceChildren();
    fetch(url)
        .then(response => {
            if (response.ok == false || response.status != 200) {
                throw new Error(`${response.status} ${response.statusText}`);
            }

            return response.json();
        })
        .then(handleData)
        .catch(handleError);
}