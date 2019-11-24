for(let elem of document.getElementsByTagName("li")) {
    let result = elem.strike()
    elem.addEventListener("click", e => alert(`capturing: ${elem.value}`), true);
    
}


// <script>
//   for(let elem of document.querySelectorAll('*')) {
//     elem.addEventListener("click", e => alert(`Capturing: ${elem.tagName}`), true);
//     elem.addEventListener("click", e => alert(`Bubbling: ${elem.tagName}`));
//   }
// </script>
