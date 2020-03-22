"use strict";
//Change the date inside the bracket to the date you want to countdown to, DO NOT REMOVE the quotation marks!!!
var CountDownTo = new Date ("December 30, 2020 23:15:00").getTime();
var x = setInterval(function() {
var RightNow = new Date().getTime();
var Time = CountDownTo - RightNow;
var Days = Math.floor(Time / (1000 * 60 * 60 * 24));
var Hours = Math.floor((Time%(1000 * 60 * 60 * 24))/(1000 * 60 * 60));
var Minutes = Math.floor((Time % (1000 * 60 * 60)) / (1000 * 60));
var Seconds = Math.floor((Time % (1000 * 60)) / 1000);
document.getElementById("DTimer").innerHTML = Days; 
document.getElementById("HTimer").innerHTML = Hours;
document.getElementById("MTimer").innerHTML = Minutes;
document.getElementById("STimer").innerHTML = Seconds;
if (Time < 0) {
clearInterval(x);
document.getElementById("DTimer").innerHTML = "";
document.getElementById("HTimer").innerHTML = "";
document.getElementById("MTimer").innerHTML = "";
document.getElementById("STimer").innerHTML = "";
document.getElementById("D").innerHTML = "";
document.getElementById("M").innerHTML = "";
document.getElementById("H").innerHTML = "";
document.getElementById("S").innerHTML = "";
document.getElementById("DC").innerHTML = "";
document.getElementById("HC").innerHTML = "";
document.getElementById("MC").innerHTML = "";
document.getElementById("OI").innerHTML = "";
document.getElementById("Stand").innerHTML = "Please stand by while this site is updating";
//Loading Dots
document.getElementById("dot1").innerHTML = "."; //When the timer ends, the . appears! These dots have a loading animation
document.getElementById("dot2").innerHTML = ".";
document.getElementById("dot3").innerHTML = ".";
//End of Loading Dots
}
}, 1000);