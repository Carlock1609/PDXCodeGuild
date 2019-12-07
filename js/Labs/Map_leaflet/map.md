// map
var mymap = L.map('mapid').setView([15.505, 1], 1.6);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    accessToken: 'pk.eyJ1IjoiY2FybG9jazkwNiIsImEiOiJjazNvMjdsNnYwMHc0M2d0MzJpdG8yamxxIn0.L_ac0fmj1jp0wrM-9T_IKw'
}).addTo(mymap);

//markers
// MARKER EXAMPLE
// var marker = L.marker([51.5, -0.09]).addTo(mymap);
// CIRCLE EXAMPLE
// var circle = L.circle([51.508, -0.11], {
//     color: 'red',
//     fillColor: '#f03',
//     fillOpacity: 0.5,
//     radius: 400,
// }).addTo(mymap);

// POLYGON EXAMPLE
// var polygon = L.polygon([
//     [51.509, -0.08],
//     [51.503, -0.06],
//     [51.51, -0.047],
// ]).addTo(mymap);

// Discriptions for markers
// marker.bindPopup("<b>Hello world!</b><br>I am a popup.").openPopup();
// circle.bindPopup("I am a circle.");
// polygon.bindPopup("I am a polygon.");

// popup with a discription
// var popup = L.popup()
//     .setLatLng({ lat: "-68.6102", lng: "-47.0653" })
//     .setContent("I am a standalone popup.")
//     .openOn(mymap);

// Coordinates of user click
// var popup = L.popup();

// function onMapClick(e) {
//     popup
//         .setLatLng(e.latlng)
//         .setContent("You clicked the map at " + e.latlng.toString())
//         .openOn(mymap);
//     let mapInfo = document.querySelector("span");
//     mapInfo.textContent = e.latlng;
// }

// mymap.on('click', onMapClick);


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

function getData() {
    const url = 'https://jsonplaceholder.typicode.com/users'
    
    axios.get(url)
    .then(request => {
        getLists(request) 
    })
    .catch(error => console.log(error))
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
        let marker = L.marker(coordinates[i]).addTo(mymap);
        marker.bindPopup(`${names[i]}<br><br>
                            ${street[i]}<br><br>
                            ${apartment[i]}<br><br>
                            ${city[i]}<br><br>
                            ${zipcode[i]}<br><br>
                            `).openPopup();
    }

    // console.log(city)
    // console.log(coordinates)
    // console.log(names)
    // console.log(usernames)
    // console.log(emails)
}
getData()


// fetch('https://jsonplaceholder.typicode.com/users/1')
//   .then(response => response.json())
//   .then(json => console.log(json))

// addTo method adds variable to map
// openPopup activates bindPopup on open