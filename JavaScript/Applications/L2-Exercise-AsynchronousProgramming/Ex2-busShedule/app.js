function solve() {
    let busStart = {
        next: 'depot',
    };
    
    const arriveBtnElement = document.getElementById('arrive');
    const departBtnElement = document.getElementById('depart');
    const infoElement = document.getElementById('info');

    const url = 'http://localhost:3030/jsonstore/bus/schedulea/';

    async function depart() {
        arriveBtnElement.disabled = false;
        departBtnElement.disabled = true;

        const startUrl = url + busStart.next;
        
        try {
            const response = await fetch(startUrl);
            const data = await response.json();
            
            busStart.name = data.name;
            busStart.next = data.next;
            
            infoElement.textContent = `Next stop ${busStart.name}`;
        } catch (error) {
            arriveBtnElement.disabled = false;
            departBtnElement.disabled = false;
            
            infoElement.textContent = `Error`;
        }
    }

    async function arrive() {
        arriveBtnElement.disabled = true;
        departBtnElement.disabled = false;
        
        infoElement.textContent = `Arriving at ${busStart.name}`
    }

    return {
        depart,
        arrive
    };
}

let result = solve();