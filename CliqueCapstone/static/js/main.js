console.log("Connected")


// **PROFILE TEMPLATE**

// Hiding profile form with button
// Figure out how to reclose
updatebtn = document.querySelector('.updatebtn')
updateform = document.querySelector('.updateform')

updatebtn.addEventListener('click', function() {
    updateform.style.display = 'block';
})

postbtn = document.querySelector('.postbtn')
postform = document.querySelector('.postform')

log.addEventListener('click', function() {
    postform.style.display = 'block';
})