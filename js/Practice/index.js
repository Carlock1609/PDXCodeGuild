let x = document.getElementById("bt1")
let isPurple = false

x.addEventListener("click", function() {
    if(!isPurple) {
        document.body.style.background = "purple"
        isPurple = true
    } else {
        document.body.style.background = "white"
        isPurple = false
    }
})