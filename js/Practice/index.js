


document.querySelector("#title").addEventListener("click", (event) => myFunc(event, "SOME STRINGS"))
function myFunc(event, userString) {
    console.log(event.target)
    console.log(`${event.target.innerText} was clicked`)
    console.log(userString)
}

document.querySelector(".remove").addEventListener("click", event => {
    let list = document.querySelector(".some-list")
    let items = document.querySelectorAll(".list-item")
    console.log(items)
    // items[0].remove()
    // list.removeChild(items[0])



})

document.querySelector(".add").addEventListener("click", event => {
    let list = document.querySelector(".some-list")
    let userInput = document.querySelector(".some-input")
    let newItem = document.createElement("li")

    newItem.appendChild(document.createTextNode(userInput.value))
    // can either set class or id
    newItem.setAttribute("id", "list-item")
    list.appendChild(newItem)
})

