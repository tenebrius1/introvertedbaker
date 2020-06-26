window.onscroll = function() {minimizeNavBar()};

function minimizeNavBar() {
    if (document.body.scrollTop >= 80 || document.documentElement.scrollTop >= 80) {
        console.log("here")
        document.getElementById("navbarSupportedContent").classList.add("justify-content-end")
        document.getElementById("navbar_container").style.flexDirection = "row"
        document.getElementById("logo").style.height = "50px"
        document.getElementById("logo").style.width = "100px"
    } else {
        document.getElementById("navbarSupportedContent").classList.remove("justify-content-end")
        document.getElementById("navbar_container").style.flexDirection = "column"
        document.getElementById("logo").style.height = "100px"
        document.getElementById("logo").style.width = "200px"
    }
}