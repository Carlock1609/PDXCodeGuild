let redirect = document.querySelector("a");

function redirector() {
    let links = ["https://www.google.com/", "https://www.bing.com/", "http://www.runescape.com/", "https://unsplash.com/", "https://fonts.google.com/", "https://www.codewars.com/dashboard", "https://www.codewars.com/dashboard", "https://colours.neilorangepeel.com/"];
    link = links[Math.floor(Math.random() * 8)]
    window.location.href = link;
}

redirect.addEventListener("click", function() {
    setTimeout(function(){redirector()}, 4000);
})