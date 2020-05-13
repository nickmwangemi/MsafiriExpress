// Dynamic Year Change on Footer
const date = new Date();
document.querySelector(".year").innerHTML = date.getFullYear();

setTimeout(function () {
  $("#message").fadeOut("slow");
}, 6000);


// Date of booking
let d = new Date();

// Set the value of the "date" field
document.getElementById("date_of_booking").value = d.toDateString();

// Set the value of the "time" field
var hours = d.getHours();
var mins = d.getMinutes();
var seconds = d.getSeconds();
document.getElementById("time").value = hours + ":" + mins + ":" + seconds;




let number_of_tickets = document.getElementById("number_of_tickets").value = 1;
let price =  document.getElementById("price").value;

if (number_of_tickets == 1){
  document.getElementById("total_amount_paid").innerHTML = number_of_tickets * price;


}
else{
  document.getElementById("number_of_tickets").addEventListener("change", function( event ) {
    var number_of_tickets = parseInt(event.target.value);
    var price = document.getElementById("price").value;
    document.getElementById("total_amount_paid").innerHTML = number_of_tickets * price;
  }, false);

}








// Data Picker Initialization - Index Page
$('.datepicker').pickadate();