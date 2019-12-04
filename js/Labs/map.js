// DONT COMMIT API KEYS

// map
var mymap = L.map('mapid').setView([15.505, 1], 1.6);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    accessToken: 'API KEY GOES HERE'
}).addTo(mymap);

var myIcon = L.icon({
    iconUrl: 'temp_pics/icon_flag.png',
    iconSize: [38, 95],
    iconAnchor: [22, 94],
    popupAnchor: [-3, -76],
    shadowSize: [68, 95],
    shadowAnchor: [22, 94]
});

// JSONPLACEHOLDER EXAMPLES
let coordinates = []
let coordLat = []
let coordLng = []
let names = []
let street = []
let apartment = []
let city = []
let zipcode = []
let usernames = []
let emails = []
let currentWeather = []

// figure out what fetch is?
function getData() {
    const url = 'https://jsonplaceholder.typicode.com/users'
    
    axios.get(url)
    .then(request => {
        getLists(request)
    })
    .catch(error => console.log(error))
} 

function getWeatherData(lat, lon) {
    const url = `http://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=API KEY GOES HERE`

    axios.get(url)
    .then(request => {
        weatherData(request)
    })
    .catch(error => console.log(error))
}

function weatherData(request) {
    let addWeather = request.data.main.temp
    currentWeather.push(addWeather)
    }


// get data
function getLists(request) {
    for(let ele of request.data) {
        let addLat = ele.address.geo.lat
        let addLng = ele.address.geo.lng
        let addNames = ele.name
        let addSt = ele.address.street
        let addApt = ele.address.suite
        let addCity = ele.address.city
        let addZip = ele.address.zipcode
        let addUsernames = ele.username
        let addEmails = ele.email

        coordinates.push([addLat, addLng])
        names.push(addNames)
        street.push(addSt)
        apartment.push(addApt)
        city.push(addCity)
        zipcode.push(addZip)
        usernames.push(addUsernames)
        emails.push(addEmails)
    }
    for(let i = 0; i < coordinates.length; i++) {
        let marker = L.marker(coordinates[i], {icon: myIcon}).addTo(mymap);
        marker.bindPopup(`
            ${names[i]}<br><br>
            ${street[i]}<br><br>
            ${apartment[i]}<br><br>
            ${city[i]}<br><br>
            ${zipcode[i]}<br><br>
        `);
        let newList = document.querySelector("ul");
        let newEle = document.createElement("li");

        newEle.appendChild(document.createTextNode(`Name: ${names[i]} | Username: ${usernames[i]} | Email: ${emails[i]}`));
        newList.appendChild(newEle);
        
        // FIGURE OUT HOW TO GET CURRENT USER ON TOP
        // for(let i = 0; i < coordinates.length; i++) {
        //     name1Div.textContent = names[i]
        //     username1Div.textContent = usernames[i]
        //     email1Div.textContent = emails[i]
        // }
        // getWeatherData(coordinates[i][i], coordinates[i][i+1])
    }
    
}

getData()

// for(let i = 0; i < coordinates.length; i++) {
//     getWeatherData(coordinates[i][i], coordinates[i][i+1])
// }
// for(let i = 0; i < coordinates.length; i++) {
//     getWeatherData(coordinates[i][i], coordinates[i][i+1])
// }
// getWeatherData(coordinates[0][0], coordinates[0][1])


// addTo method adds variable to map
// openPopup activates bindPopup on open

// addEle.addEventListener("click", function() {
//     let lis = document.querySelectorAll("li");
//     for(let i = 0; i < lis.length; i++) {
//       lis[i].addEventListener("mouseover", function() {
//         this.classList.add("selected");
//       });


// WEATHER API