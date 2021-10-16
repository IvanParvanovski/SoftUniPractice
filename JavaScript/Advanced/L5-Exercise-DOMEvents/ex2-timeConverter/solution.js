function attachEventsListeners() {
    const ratios = {
        days: 1,
        hours: 24,
        minutes: 1440,
        seconds: 86400,
    }

    function convert(value, unit) {
        const inDays = value / ratios[unit];

        return {
            days: inDays,
            hours: inDays * ratios.hours,
            minutes: inDays * ratios.minutes,
            seconds: inDays * ratios.seconds,
        };
    }

    const inputs = {
        days: document.getElementById('days'),
        hours: document.getElementById('hours'),
        minutes: document.getElementById('minutes'),
        seconds: document.getElementById('seconds'),
    }

    document.querySelector('main').addEventListener('click', onConvert);

    function onConvert(event) {
        const input = event.target.parentElement.querySelector('input[type="text"]');
        const time = convert(Number(input.value), input.id);
        
        Object.keys(inputs).forEach((k) => setTime(time, k));
    }

    function setTime(time, unit) {
        inputs[unit].value = time[unit];
    }
}