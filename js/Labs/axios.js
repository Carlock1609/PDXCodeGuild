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
let span = document.querySelector("span")
let footer = document.querySelector("footer")

function main() {
    (function() {
        const url = "https://favqs.com/api/qotd"
        axios.get(url)
            .then(request =>  getAuthor(request))
            .catch(error => console.log(error))
    })()
}

function getAuthor(request) {
    span.textContent = request.data.quote.body
    footer.textContent = request.data.quote.author
}

main()