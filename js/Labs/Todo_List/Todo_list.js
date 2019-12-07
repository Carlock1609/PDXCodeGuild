let addEle = document.getElementById("add");
let remEle = document.getElementById("remove");

addEle.addEventListener("click", function() {
  let newList = document.querySelector("ul");
  let userInput = document.getElementById("someInput");
  let newEle = document.createElement("li");

  newEle.appendChild(document.createTextNode(userInput.value));
  newList.appendChild(newEle);
});

addEle.addEventListener("click", function() {
  let lis = document.querySelectorAll("li");
  for(let i = 0; i < lis.length; i++) {
    lis[i].addEventListener("mouseover", function() {
      this.classList.add("selected");
    });
    lis[i].addEventListener("mouseout", function() {
      this.classList.remove("selected");
    });
    lis[i].addEventListener("click", function() {
      this.classList.toggle("done");
    });
  };
})

// working on removing li
remEle.addEventListener("click", function() {
  let lis = document.querySelectorAll("li");
  for(let i = 0; i < lis.length; i++){
      if(lis[i].classList.contains("done")) {
        lis[i].remove()
        console.log("ladkasddlk")
      }
    }
})


// get remove to work
// remEle.addEventListener("click", function() {
//   newEle[-1].remove()
// })
// document.querySelector("element").addEventListener("click", event => {
//   event.target.remove()
// })



//move incomplete taks to completed tasks
// document.querySelector("class").addEventListener("click", event => {
//   event.target.classList.remove("class")
//   event.target.classList.add("class")
//   document.querySelector("class").append(event.target);
// })

