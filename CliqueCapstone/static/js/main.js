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
  if(postform.style.display == 'block') {
    postform.style.display = 'none'
  }
  else {
    postform.style.display = 'block';
  }
})

// image_ = document.querySelector('.profile_photo_btn')
// delete_btn = document.querySelector('#delete_btn')

// profile_photo_btn.addEventListener('mouseover', function() {
//   if(delete_btn.style.display == 'block') {
//     delete_btn.style.display = 'none'
//   }
//   else {
//     delete_btn.style.display = 'block'
//   }
// })
// profile_photo_btn.addEventListener('mouseout', function() {
//   if(delete_btn.style.display == 'block') {
//     delete_btn.style.display = 'none'
//   }
//   else {
//     delete_btn.style.display = 'block'
//   }
// })