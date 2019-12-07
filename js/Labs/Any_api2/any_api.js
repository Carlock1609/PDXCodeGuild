function getWeatherData() {
    let input = document.querySelector("input")
    let submit = document.querySelector("span")
    let zipcode = ""

    submit.addEventListener("click", function() {
        zipcode = input.textContent
    })

    const url = `https://api.openweathermap.org/data/2.5/weather?zip=${input},us&units=imperial&appid=${keyWeatherAPI}`

    axios.get(url)
    .then(request => {
        console.log(request.data)
    })
    .catch(error => console.log(error))
}

// function showWeather() {

// }

getWeatherData()




// https://tile.openweathermap.org/map/{layer}/{z}/{x}/{y}.png?appid={api_key}

