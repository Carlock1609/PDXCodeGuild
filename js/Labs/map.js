// DONT COMMIT API KEYS

// map
var mymap = L.map('mapid').setView([15.505, 1], 1.6);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    accessToken: 'API HERE'
}).addTo(mymap);

var myIcon = L.icon({
    iconUrl: 'temp_pics/icon_flag.png',
    iconSize: [38, 95],
    iconAnchor: [22, 94],
    popupAnchor: [-3, -76],
    shadowSize: [68, 95],
    shadowAnchor: [22, 94]
});

// figure out what fetch is?
function getData() {
    const url = 'https://jsonplaceholder.typicode.com/users'
    
    axios.get(url)
    .then(request => 
        getLists(request))
    
    .catch(error => console.log(error))
} 

function getWeatherData(lat, lon) {
    const url = `http://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=API HERE`

    axios.get(url)
    .then(request => {
        console.log(request.data)
    })
    .catch(error => console.log(error))
}

// JSONPLACEHOLDER EXAMPLES
// use an object instead

// request call to get data for arr
function getDataList() {
    let dataList = {
        "coordinates": [],
        "coordLat": [],
        "coordLng": [],
        "names": [],
        "street": [],
        "apartment": [],
        "city": [],
        "zipcode": [],
        "usernames": [],
        "emails": [],
        }
    return dataList
}

function getLists(request, dataList) {
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

        dataList.coordinates.push([addLat, addLng])
        dataList.names.push(addNames)
        dataList.street.push(addSt)
        dataList.apartment.push(addApt)
        dataList.city.push(addCity)
        dataList.zipcode.push(addZip)
        dataList.usernames.push(addUsernames)
        dataList.emails.push(addEmails)
    }
}
function getIcons(dataList) {
    for(let i = 0; i < 11; i++) {
        let marker = L.marker(dataList.coordinates[i], {icon: myIcon}).addTo(mymap);
        marker.bindPopup(`
            ${dataList.names[i]}<br><br>
            ${dataList.street[i]}<br><br>
            ${dataList.apartment[i]}<br><br>
            ${dataList.city[i]}<br><br>
            ${dataList.zipcode[i]}<br><br>
        `);
        let newList = document.querySelector("ul");
        let newEle = document.createElement("li");

        newEle.appendChild(document.createTextNode(`Name: ${dataList.names[i]} | Username: ${dataList.usernames[i]} | Email: ${dataList.emails[i]}`));
        newList.appendChild(newEle);
    }
}

    // Trying to figure out how to add curent selection
    // let x = document.querySelectorAll("img");
    // let name1Div = document.querySelector("#name1Div");
    // let email1Div = document.querySelector("#email1Div");
    //     for(let i = 0; i < names.length; i++){
    //         x[i].addEventListener("click", function() {
    //             this.name1Div.textContent = names[i];
    //             this.email1Div.textContent = emails[i];
    //         })
    //     }

getData();

// console.log(getDataList())
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