// arrow function, if only one parameter, no () needed
let myPrint = num => console.log("Fuck")
// OR
const myNewAdd = (a,b) => a + b
// OR
let myAdd = (a,b) => {
    a=5;
    b=5;
    a + b
}

// call back functions
// not working
// function greeting(name) {
//     alert("Hello " + name)
// }

// function processUserInput(callback) {
//     let name = ("Jon");
//     callback(name);
// };

// processUserInput(greeting);

user-content-callbacks

// EVENTS
<button id="bt">Click</button>
x = document.querySelector("#bt")
x.addEventListener("click", function() {
    alert("Hello World")
})


// PHASE
// CAPTURE PHASE(1) - goes to target
// TARGET PHASE(2) - target
// BUBBLING PHASE(3) - bubbles back up to capture