function attachEvents() {
    const weatherSymbols = {
        'Sunny': '☀',
        'Partly sunny': '⛅',
        'Overcast': '☁',
        'Rain': '☂',
        'Degrees': '°',
    };

    const displayWeatherBtnElement = document.getElementById('submit');
    displayWeatherBtnElement.addEventListener('click', displayWeather);
    
    const searchedLocationElement = document.getElementById('location');
   
    const forecastElement = document.getElementById('forecast');
    const currentWeatherSection = forecastElement.querySelector('#current');
    const upcomingWeatherSection = forecastElement.querySelector('#upcoming');
    
    async function displayWeather(event) {
        const searchedLocationName = searchedLocationElement.value;
        currentWeatherSection.replaceChildren();
        upcomingWeatherSection.replaceChildren();
        
        const lastSection = forecastElement.lastElementChild;
        if ([...lastSection.classList].includes('error')) {
            forecastElement.removeChild(lastSection);
        }

        try {
            const searchedLocation = await getLocation(searchedLocationName);

            const [currentWeather, upcomingWeather] = await Promise.all([
                getCurrentWeather(searchedLocation.code),
                getUpcomingWeather(searchedLocation.code),
            ]);

            console.log(typeof upcomingWeather);
            if (typeof(currentWeather) != 'object' || typeof(upcomingWeather) != 'object') {
                throw new Error(`Invalid weather data!`)
            }

            fillInCurrentWeatherSection(currentWeather);
            fillInUpcomingWeatherSection(upcomingWeather);
            
            forecastElement.style.display = 'block';
        } catch (error) {
            const errorDiv = document.createElement('div');
            errorDiv.classList.add('label');
            errorDiv.classList.add('error');
            errorDiv.textContent = 'Error';

            forecastElement.appendChild(errorDiv);
            forecastElement.style.display = 'block';
            console.error(error);
        }   
        
        console.log();
    }

    function fillInCurrentWeatherSection(currentWeather) {
        // Create Heading
        const currentWeatherHeader = document.createElement('div');
        currentWeatherHeader.classList.add('label'); 
        currentWeatherHeader.textContent = 'Current conditions';

        // Get Inner Content
        const currentWeatherElement = createCurrentWeatherDataElement(currentWeather);
                    
        // Append to the Current Weather Section
        currentWeatherSection.appendChild(currentWeatherHeader);
        currentWeatherSection.appendChild(currentWeatherElement);
    }

    function fillInUpcomingWeatherSection(upcomingWeather) {
        // Create Heading
        const upcomingWeatherHeading = document.createElement('div');
        upcomingWeatherHeading.classList.add('label');
        upcomingWeatherHeading.textContent = 'Three-day forecast';

        // Get Inner Content
        const upcomingWeatherElement = createUpcomingWeatherDataElement(upcomingWeather);

        // Append to the Upcoming Weather Section
        upcomingWeatherSection.appendChild(upcomingWeatherHeading);
        upcomingWeatherSection.appendChild(upcomingWeatherElement);
    }

    function createUpcomingWeatherDataElement(upcomingWeather) {        
        const newForecast = document.createElement('div');
        newForecast.classList.add('forecasts-info');

        for (const weatherData of upcomingWeather.forecast) {
            const newUpcomingCondition = document.createElement('span');
            newUpcomingCondition.classList.add('upcoming')
            newUpcomingCondition.innerHTML = [
                `<span class='symbol'>${weatherSymbols[weatherData.condition]}</span>`,
                `<span class='forecast-data'> 
                    ${weatherData.low}${weatherSymbols['Degrees']}/
                    ${weatherData.high}${weatherSymbols['Degrees']}
                </span>`,
                `<span class="forecast-data'>${weatherData.condition}</span>`,
                `<span class="forecast-data'>${weatherData.condition}</span>`
            ].join('');

            console.log(newUpcomingCondition)
            
            newForecast.appendChild(newUpcomingCondition);
        }

        return newForecast;
    }

    function createCurrentWeatherDataElement(currentWeather) {
        const newForecast = document.createElement('div');
        newForecast.classList.add('forecasts');

        const conditionSymbol = document.createElement('span');
        conditionSymbol.classList.add('condition');
        conditionSymbol.classList.add('symbol');
        conditionSymbol.textContent = weatherSymbols[currentWeather.forecast.condition];

        const condition = document.createElement('span');
        condition.classList.add('condition')
        condition.innerHTML = [
            `<span class='forecast-data'>${currentWeather.name}</span>`,
            `<span class='forecast-data'> 
                ${currentWeather.forecast.low}${weatherSymbols['Degrees']}/
                ${currentWeather.forecast.high}${weatherSymbols['Degrees']}
            </span>`,
            `<span class="forecast-data'>${currentWeather.forecast.condition}</span>`
        ].join('');

        newForecast.appendChild(conditionSymbol);
        newForecast.appendChild(condition);

        return newForecast;
    }

    async function getLocation(name) {
        const url = 'http://localhost:3030/jsonstore/forecaster/locations';
        const locations = await sendRequest(url);
        const searchedLocation = locations.find(x => x.name == name);
        
        if (searchedLocation == undefined) {
            throw new Error('Location does not exist!');
        }

        return searchedLocation;
    } 

    function getCurrentWeather(code) {
        const url = 'http://localhost:3030/jsonstore/forecaster/today/' + code;
        return sendRequest(url);
    }

    function getUpcomingWeather(code) {
        const url = 'http://localhost:3030/jsonstore/forecaster/upcoming/' + code;
        return sendRequest(url);
    }

    async function sendRequest(url) {
        const response = await fetch(url);
        
        if (response.status != 200) {
            throw new Error(`${response.status} ${response.statusText}`);
        }

        const data = await response.json();
        return data;
    }
}

attachEvents();