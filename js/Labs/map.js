// DONT COMMIT API KEYS

// map
let mymap = L.map('mapid', {
        worldCopyJump: true,
    })
    .setView([0, 0], 3);

L.tileLayer(`https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=${keyMapbox}`, {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    accessToken: "your.mapbox.access.token"
}).addTo(mymap);

// figure out what fetch is?
function getData() {
    const url = 'https://jsonplaceholder.typicode.com/users'
    
    axios.get(url)
    .then(request => 
        getLists(request))
    
    .catch(error => console.log(error))
} 

// WEATHER API FEATURE
// function getWeatherData(lat, lon) {
//     const url = `http://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&units=imperial&appid=${keyWeatherAPI}`

//     axios.get(url)
//     .then(request => {
//         console.log(request.data.main.temp)
//     })
//     .catch(error => console.log(error))
// }

// JSONPLACEHOLDER EXAMPLES
function getLists(request) {
    let coord = []
    for(let ele of request.data) {
        let addCoord = [ele.address.geo.lat, ele.address.geo.lng]
        let addName = ele.name
        let addStreet = ele.address.street
        let addSuite = ele.address.suite
        let addCity = ele.address.city
        let addZipcode = ele.address.zipcode
        let addEmail = ele.email
        let addUsername = ele.username

        let marker = L.marker(addCoord).addTo(mymap);
            marker.bindPopup(`
                ${addName}<br><br>
                ${addStreet}<br><br>
                ${addSuite}<br><br>
                ${addCity}<br><br>
                ${addZipcode}
                `);
        coord.push(addCoord)

        let newList = document.querySelector("ul");
        let newEle = document.createElement("li");

        newEle.appendChild(document.createTextNode(`Name: ${addName} | Username: ${addUsername} | Email: ${addEmail}`));
        newList.appendChild(newEle);
    }
    
}

function main() {
    getData()
}
main();
