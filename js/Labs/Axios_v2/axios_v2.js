// DO NOT PUSH API KEY TO GITHUB

let quotes = []
let authors = []
let div = document.getElementById("quote")
let footer = document.querySelector("footer")
let start = document.querySelector("a")

function getData(userInput) {
    const url = 'https://favqs.com/api/quotes?filter=' + userInput
    
    axios.get(url, {
        headers: {
            'Authorization': `Token token="ADD API KEY HERE"`
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
        let addAuthor = quote.author
        authors.push(addAuthor)
        quotes.push(addBody)
    
    }
    let x = Math.floor(Math.random() * quotes.length)
    div.textContent = quotes[x]
    footer.textContent = authors[x]

}

start.addEventListener("click", function() {
    let userInput = prompt("Enter in a WORD to get related QUOTES.")
    getData(userInput)
})

