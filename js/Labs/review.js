const url = "https://randomuser.me/api/";

function getData() {
axios.get(url)
    .then(request => { console.log(request.data);
        document.querySelector("#name").innerText += ` ${request.data.results[0].name.first} ${request.data.results[0].name.last}`;
        document.querySelector("#username").innerText += ` ${request.data.results[0].login.username}`;
        document.querySelector("#email").innerText += ` ${request.data.results[0].email}`;
        document.querySelector("#phone").innerText += ` ${request.data.results[0].phone}`;
        document.querySelector("#street").innerText += ` ${request.data.results[0].location.street.number} ${request.data.results[0].location.street.name}`;
        document.querySelector("#city").innerText += ` ${request.data.results[0].location.city}`;
        document.querySelector("#state").innerText += ` ${request.data.results[0].location.state}`;
        document.querySelector("#zip").innerText += ` ${request.data.results[0].location.postcode}`;
    })
    .catch(error => console.log(error))
};

function moveCookies() {
    let oldCookies = document.querySelector("#cookie-jar").textContent;
    let newCookies = document.querySelector("#newJar");

    newCookies.textContent = oldCookies;
    document.querySelector("#cookie-jar").remove();
}
function makePretty() {
    let strings = document.querySelector("#pretty").textContent;
    let r = Math.floor(Math.random() * 255)
    let g = Math.floor(Math.random() * 255)
    let b = Math.floor(Math.random() * 255)
    console.log(strings[])
    for(let ele of strings) {
        document.querySelector("#pretty").style.color = `rgb(${r}, ${g}, ${b})`
        }
    
    
    // for(let ele of strings) {
    //     ele.style.color = "red"
    // }


        // ele.style.color = "blue"
    
}

function main() {
    getData();
    moveCookies();
    makePretty();
}
main();

