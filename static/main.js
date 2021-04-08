
console.log("!");

// Get Stripe publishable key
fetch("/config/")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);

  // new
  // Event handler
  let monthly = document.querySelector("#monthly");
  if (monthly !== null) {
    monthly.addEventListener("click", () => {
    // Get Checkout Session ID
    fetch("/create-checkout-session/1/")
      .then((result) => { return result.json(); })
      .then((data) => {
        console.log(data);
        // Redirect to Stripe Checkout
        return stripe.redirectToCheckout({sessionId: data.sessionId})
      })
      .then((res) => {
        console.log(res);
      });
    });
  }

  let bianually = document.querySelector("#bianually");
  if (bianually !== null) {
    bianually.addEventListener("click", () => {
    // Get Checkout Session ID
    fetch("/create-checkout-session/2/")
      .then((result) => { return result.json(); })
      .then((data) => {
        console.log(data);
        // Redirect to Stripe Checkout
        return stripe.redirectToCheckout({sessionId: data.sessionId})
      })
      .then((res) => {
        console.log(res);
      });
    });
  }

  let anaually = document.querySelector("#anaually");
  if (anaually !== null) {
    anaually.addEventListener("click", () => {
    // Get Checkout Session ID
    fetch("/create-checkout-session/3/")
      .then((result) => { return result.json(); })
      .then((data) => {
        console.log(data);
        // Redirect to Stripe Checkout
        return stripe.redirectToCheckout({sessionId: data.sessionId})
      })
      .then((res) => {
        console.log(res);
      });
    });
  }
});
