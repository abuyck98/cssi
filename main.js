//console.log("what up");
//console.log(2 + 2);

function checkout (item1, item2, coupon) {
  var subtotal = item1 + item2;
  var couponValue = subtotal * coupon;
  var grandTotal = subtotal - couponValue;
  //console.log(grandTotal);
  return grandTotal;
}

console.log(checkout(33, 19, .15));

var bananaPrice = 1.5;
var pudding = 6;
var coupon = .2;

var bankAccount = 350;

var remainAmount = bankAccount - checkout(bananaPrice, pudding, coupon);

console.log("Total amount left in bank: " + remainAmount);
