console.log("Connected")

// **PROFILE TEMPLATE**
postbtn = document.querySelector('.postbtn')
postform = document.querySelector('.postform')

postbtn.addEventListener('click', function() {
    postform.style.display = 'block';
})


// NAVBAR SCROLL
let prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  let currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.querySelector(".navbar").style.top = "0";
  } else {
    document.querySelector(".navbar").style.top = "-56px";
  }
  prevScrollpos = currentScrollPos;
} 