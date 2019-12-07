// (function() {
//     const url = "https://jsonplaceholder.typicode.com/posts/"
//     axios.get(url)
//     .then(request => console.log(request.data))
//     .catch(error => console.log(error))
// })()

//CHUCK NORRIS JOKES
// (function() {
//     const url = "https://api.icndb.com/jokes/random"
//     axios.get(url, {
//         params: {
//             limitTo: "[nerdy]",
//         }
//     })
//     .then(request => console.log(request.data))
//     .catch(error => console.log(error))
// })()


// VERSION 1 DONE
let quote = document.querySelector("#quote")
let footer = document.querySelector("footer")
let reset = document.querySelector("a")

function findData() {
    (function() {
        const url = "https://favqs.com/api/qotd"
        axios.get(url)
            .then(request =>  getData(request))
            .catch(error => console.log(error))
    })()
}

function getData(request) {
    quote.textContent = request.data.quote.body
    footer.textContent = request.data.quote.author
}

findData()
reset.addEventListener("click", function() {
    findData()
})