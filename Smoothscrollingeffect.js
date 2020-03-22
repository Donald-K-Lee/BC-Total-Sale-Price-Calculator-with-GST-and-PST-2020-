//Smooth Scrolling Effect
$(document).ready(function(){
  // Add smooth scrolling to links
  $("a").on('click', function(event) {
    if (this.hash !== "") {
      event.preventDefault();
      var hash = this.hash;
      //The number defines the number of milliseconds it takes to scroll
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 1000, function(){
        window.location.hash = hash;
      });
    } 
  });
});