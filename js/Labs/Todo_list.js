let addEle = document.getElementById("add")
let remEle = document.getElementById("remove")
let strikeEle = document.getElementById("todo-item")

addEle.addEventListener("click", event => {
    let newList = document.getElementById("todos")
    let userInput = document.getElementById("someInput")
    let newEle = document.createElement("li")

    newEle.appendChild(document.createTextNode(userInput.value))
    newEle.setAttribute("id", "todo-item")
    newList.appendChild(newEle)
})

strikeEle.addEventListener("click", event => {
    strikeEle.style.textDecoration = "line-through"
})





// wait to edit until click on add and it moves over
// remEle.addEventListener("click", event => {
//     let doneList = document.getElementById("done")
//     let userInput = document.getElementById("someInput")
//     let newEle = document.createElement("li")

//     newEle.appendChild(document.createTextNode(userInput.value))
//     newEle.setAttribute("id", "list-item")
//     doneList.appendChild(newEle)
// })
