//console.log("what up");
//console.log(2 + 2);

//function checkout (item1, item2, coupon, salesTax) {
  //var subtotal = item1 + item2;
  //var salesTax = .0725;
  //var couponValue = subtotal * coupon;
  //var grandTotal = subtotal - couponValue;
  //console.log(grandTotal);
  //return grandTotal;
//}

//checkout(50, 25, .25, .0725);

//var bananaPrice = 1.5;
//var pudding = 6;
//var bankAccount = 350;

//var remainAmount = bankAccount - checkout(bananaPrice, pudding, coupon);

//console.log("Total amount left in bank: " + remainAmount);

//var test = jQuery("#purple-colored-heading");
//test.text("who cares?");

//var elevatorLine = [];

//function pressFloorNumber (elevatorLine, floorPressed) {
  //elevatorLine.push(floorPressed);
  //console.log ("position " + elevatorLine.length);
//}

//function goToNextFloor () {
  //if (elevatorLine.length == 0) console.log ("There are no more floors to go to!");
  //else {
    //console.log(elevatorLine[0])
    //elevatorLine.splice(0, 1);
  //}
//}

//function currentLine (elevatorLine){
  //var index = 0;
  //while(index < elevatorLine.length) {
    //console.log(" floor " + elevatorLine[index])
    //index++;
  //}
//}

//function niceRegularBox (console.log("string")) {
  //console.log("pie", "is", "good" + "?");
  //}

function myGreeting() {
  console.log('button was clicked')
  var userName = $('#username').val();
  console.log(userName);
  var userAge = $('#userage').val();
  console.log(userAge);
  $('#purple-colored-heading').text('What are you doing here ' + userName + '???')
}

function setup() {
  console.log('page is ready!!');
  $('#submitButton').click(myGreeting);
}


$(document).ready(setup);
