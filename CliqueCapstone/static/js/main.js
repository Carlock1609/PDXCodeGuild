console.log("Connected")

// **NAVBAR**

// navbar scroll
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

// fading links
// fading_nav = document.querySelector('#fading_nav')
// fading_nav.addEventListener('hover', function() {
//   alert('you got him')
//     fading_nav.style.color = 'black'
// })

// **PROFILE TEMPLATE**
postbtn = document.querySelector('.postbtn')
postform = document.querySelector('.postform')

postbtn.addEventListener('click', function() {
    postform.style.display = 'block';
})


