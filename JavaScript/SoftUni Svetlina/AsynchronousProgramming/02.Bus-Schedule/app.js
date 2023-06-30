function solve() {
    const infoDiv = document.querySelector('span.info');
    
    const departBtn = document.getElementById('depart');
    const arriveBtn = document.getElementById('arrive');
    
    let currentStopName = 'depot';
    let nextStopName;

    async function depart() {
        departBtn.disabled = true;
        arriveBtn.disabled = false;

        currentStop = await (await fetch(`http://localhost:3030/jsonstore/bus/schedule/${currentStopName}`)).json();
        nextStopName = currentStop.next;

        infoDiv.innerHTML = currentStop.name;   
    }

    function arrive() {
        departBtn.disabled = false;
        arriveBtn.disabled = true;

        currentStopName = nextStopName;
    }

    return {
        depart,
        arrive
    };
}

let result = solve();
console.log(result);
