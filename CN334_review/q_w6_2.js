const products = [
    { id: 1, name: "Keyboard", price:500 },
    { id: 2, name: "Mouse", price:300},
    { id: 3, name: "Monitor", price:5000}
];

function calculationTotal() {
    const total = products.reduce((sum, product) => sum + product.price, 0);
    document.getElementById("totalPrice").innerText = `Total Price: ${total} THB`;

}

window.onload = calculationTotal;