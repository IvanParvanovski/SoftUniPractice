function attachEventsListeners() {
    document.getElementById('convert').addEventListener('click', onClick);
    
    function onClick(event) {
        const inputDistance = document.getElementById('inputDistance').value;
        const outputDistanceElement = document.getElementById('outputDistance');

        const inputUnit = document.getElementById('inputUnits').value;
        const outputUnit = document.getElementById('outputUnits').value;
        
        const outputDistance = convert(inputDistance, inputUnit, outputUnit);
        outputDistanceElement.value = outputDistance;
    }

    function convert(distance, inputUnit, outputUnit) {
        const units = {
            km: 1000,
            m: 1,
            cm: 0.01,
            mm: 0.001,
            mi: 1609.34,
            yrd: 0.9144,
            ft: 0.3048,
            in: 0.0254, 
        }
    
        const distanceInM = Number(distance) * units[inputUnit];
        return distanceInM / units[outputUnit];
    }    
}

