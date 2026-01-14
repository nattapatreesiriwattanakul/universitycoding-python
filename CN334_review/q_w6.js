const products = [
    {id: 1, name: "Keyboard", price:500},
    {id: 2, name: "Mouse", price:300 },
    {id: 3, name: "Monitor", price:5000}
];

function displayProducts() {
    const tableBody = document.getElementById("productTable");
    tableBody.innerHTML = "";
    products.forEach((product, index) => {
        let row = `
            <tr>
                <td>${index + 1}</td>
                <td>${product.name}</td>
                <td>${product.price}</td>
            </tr>
        `;
        tableBody.innerHTML += row
    });
}

window.onload = displayProducts;