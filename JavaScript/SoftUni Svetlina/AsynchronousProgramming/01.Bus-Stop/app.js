const stopName = document.getElementById('stopName');
const buses = document.getElementById('buses');

async function getInfo() {
    const busStopId = document.getElementById('stopId').value;

    try {
        const busStop = await (await fetch(`http://localhost:3030/jsonstore/bus/businfo/${busStopId}`)).json();
        stopName.innerHTML = busStop.name;

        for (const busId in busStop.buses) {
            const li = document.createElement('li');
            li.innerText = `Bus ${busId} arrives in ${busStop.buses[busId]}`; 

            buses.appendChild(li)
        }
    } catch(err) {
        console.log(err);
        stopName.innerHTML = 'Error';
    }
}
