// Back To Top Button 
mybutton = document.getElementById("TopBtn");
window.onscroll = function() {
    if (document.body.scrollTop > 1000 || document.documentElement.scrollTop > 1000) {
      mybutton.style.display = "block";
    } else {
      mybutton.style.display = "none";
    }
  }

  function goToTop() {
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
  } 