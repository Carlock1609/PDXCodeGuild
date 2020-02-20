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

if (document.querySelector('#chat_box')) {
  let chat_box = document.querySelector('#chat_box')
  chat_box.scrollTop = chat_box.scrollHeight;
}

// **PROFILE TEMPLATE**

// Get the modal
let modal = document.querySelector("#myModal");
// Get the image
let images = document.querySelectorAll("#myImg");
for(let i=0; i<images.length; i++) {
  images[i].addEventListener("click", function() {
    images.id = "myImg"
    modal.style.display = "block";
    modalImg.src = this.src;
  })
}

// THIS IS CAUSING ISSUES WITH PLACEMENT
postbtn = document.querySelector('.postbtn')
postform = document.querySelector('.postform')

postbtn.addEventListener('click', function() {
  if(postform.style.display == 'block') {
    postform.style.display = 'none'
  }
  else {
    postform.style.display = 'block'
  }
})

// BUG THIS GOES WITH THE MODAL
let modalImg = document.querySelector("#img01");
// Get the <span> element that closes the modal
let span = document.getElementsByClassName("close")[0];
span.addEventListener('click', function() {
  modal.style.display = "none";
}) 



// expandinfo = document.querySelector('.expandinfo')
// info = document.querySelector('.info')

// expandinfo.addEventListener('click', function() {
  //   if(info.style.display == 'block') {
    //     info.style.display = 'none'
    //   }
    //   else {
//     info.style.display = 'block'
//   }
// })


// Get the modal
// let modal = document.getElementById("myModal");
// Get the image and insert it inside the modal - use its "alt" text as a caption
// let img = document.querySelector(".myImg");
// let modalImg = document.getElementById("img01");
// let captionText = document.getElementById("caption");
// img.addEventListener('click', function() {
  //   modal.style.display = "block";
  //   modalImg.src = this.src;
  //   captionText.innerHTML = this.alt;
  // })
  // Get the <span> element that closes the modal
  // let span = document.getElementsByClassName("close")[0];
// When the user clicks on <span> (x), close the modal
// span.onclick = function() {
  //   modal.style.display = "none";
// } 



// chat_box.scrollTop += chat_box.scrollHeight;

// $(document).on('submit', '#add_friend', function(e) {
  //     e.preventDefault();
  
  //     $.ajax({
    //       type:'POST',
    //       url:'/users/profile/6/',
    //       data:{
      //         friends_list:$('#friends_list').val(),
      //         csrfmiddlewaretoken:$('input[friends_list=csrfmiddlewaretoken]').val()
      //         },
      //         success:function(){
        //           alert('Added Friend!')
        
        //         }
        //     })
        // })
        
        
        
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
// fading links
// fading_nav = document.querySelector('#fading_nav')
// fading_nav.addEventListener('hover', function() {
//   alert('you got him')
//     fading_nav.style.color = 'black'
// })