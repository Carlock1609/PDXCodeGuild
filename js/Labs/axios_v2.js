// DO NOT PUSH API KEY TO GITHUB
let quotes = []
let userInput = prompt("Enter in a keyword to recieve a related QUOTE.")
let div = document.getElementById("quote")

function getData(userInput) {
    const url = 'https://favqs.com/api/quotes?filter=' + userInput
    
    axios.get(url, {
        headers: {
            'Authorization': `Token token="API KEY GOES HERE***"`
        }
    })
    .then(request => {
        getBody(request)
    })
    .catch(error => console.log(error))
} 

function getBody(request) {
    for(let quote of request.data.quotes) {
        let addBody = quote.body
        quotes.push(addBody)
    }
    div.textContent = quotes[Math.floor(Math.random() * quotes.length)]

}
getData(userInput)


// document.createTextNode(userInput.value)

// // V2
// function http_get(url, success) {
//     let xhttp = new XMLHttpRequest();
//     xhttp.onreadystatechange = function() {
//         if (this.readyState === 1) {
//             xhttp.setRequestHeader('Authorization', 'Token token="<api kep here>"')
//         } else if (this.readyState === 4 && this.status === 200) {
//             let data = JSON.parse(xhttp.responseText);
//             success(data);
//         } else if (this.readyState === 4 && this.status === 404) {
//             // handle 404
//         }
//     };
//     xhttp.open("GET", url);
//     xhttp.send();
// }

