// map
var mymap = L.map('mapid').setView([51.505, -0.09], 13);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    accessToken: 'API KEY HERE'
}).addTo(mymap);

//markers
var marker = L.marker([51.5, -0.09]).addTo(mymap);
var circle = L.circle([51.508, -0.11], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 400,
}).addTo(mymap);
var polygon = L.polygon([
    [51.509, -0.08],
    [51.503, -0.06],
    [51.51, -0.047],
]).addTo(mymap);

// discriptions
marker.bindPopup("<b>Hello world!</b><br>I am a popup.").openPopup();
circle.bindPopup("I am a circle.");
polygon.bindPopup("I am a polygon.");

// popup with a discription
var popup = L.popup()
    .setLatLng([51.493, -0.09])
    .setContent("I am a standalone popup.")
    .openOn(mymap);


var popup = L.popup();

function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(mymap);
    let mapInfo = document.querySelector("span");
    mapInfo.textContent = e.latlng;
}

mymap.on('click', onMapClick);

// function onMapClick(e) {
//     let mapInfo = document.querySelector("span");
//     mapInfo.textContent = e.latlng;
// }

// mymap.on('click', onMapClick);



// addTo method adds variable to map
// openPopup activates bindPopup on open