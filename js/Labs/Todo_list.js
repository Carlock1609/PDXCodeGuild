let addEle = document.getElementById("add")
let remEle = document.getElementById("remove")
let strikeEle = document.getElementById("todos")

let counter = 0

// WORKING
// addEle.addEventListener("click", event => {
//     let newList = document.getElementById("todos")
//     let userInput = document.getElementById("someInput")
//     let newEle = document.createElement("li")
    
//     newEle.appendChild(document.createTextNode(userInput.value))
//     newEle.setAttribute("id", `list-item${counter}`)
//     newEle.setAttribute("onclick", `lineThrough('list-item${counter}', '${userInput.value}')`)
//     newList.appendChild(newEle)
//     counter += 1
// })

// function lineThrough(item, userInput) {
//     let result = userInput.strike()    
//     document.getElementById(`${item}`).innerHTML = result
// }

// remEle.addEventListener("click", event => {
//     let remove = newEle.remove()
// })




/* <form id="form">FORM
    <div>DIV
      <p>P</p>
    </div>
  </form> */

//   form.onclick = function(event) {
//     event.target.style.backgroundColor = 'yellow';
  
//     // chrome needs some time to paint yellow
//     setTimeout(() => {
//       alert("target = " + event.target.tagName + ", this=" + this.tagName);
//       event.target.style.backgroundColor = ''
//     }, 0);
//   };


// <script>
//   for(let elem of document.querySelectorAll('*')) {
//     elem.addEventListener("click", e => alert(`Capturing: ${elem.tagName}`), true);
//     elem.addEventListener("click", e => alert(`Bubbling: ${elem.tagName}`));
//   }
// </script>

// x.addEventListener("click", lineThrough => {
//     x.style.color = "pink"
// })

// function lineThrough() {
//     let x = document.getElementsByTagName("li")
//     x.style.color = "pink"
// }

// wait to edit until click on add and it moves over
// remEle.addEventListener("click", event => {
//     let doneList = document.getElementById("done")
//     let userInput = document.getElementById("someInput")
//     let newEle = document.createElement("li")

//     newEle.appendChild(document.createTextNode(userInput.value))
//     newEle.setAttribute("id", "list-item")
//     doneList.appendChild(newEle)
// })


// let btn = document.getElementById('testbtn');
// btn.addEventListener('click', function(blargle){
//     print_event(blargle);
// });

// function print_event(blargle){
//     console.log(blargle);

//     event.target.remove();
// }
