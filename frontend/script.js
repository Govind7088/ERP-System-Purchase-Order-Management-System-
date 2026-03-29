const toggle = document.getElementById("menu-toggle");
const menu = document.getElementById("menu");

toggle.addEventListener("click", () => {
  menu.classList.toggle("active");
});

const API = "http://127.0.0.1:8000";

// Load Vendors
fetch(API + "/vendors")
.then(res => res.json())
.then(data => {
    console.log("API Response:", data);  //  check this

    if (!data || !Array.isArray(data)) {
        console.error("Invalid data:", data);
        return;
    }

    let dropdown = document.getElementById("vendors");

    data.forEach(v => {
        let option = `<option value="${v.id}">${v.name}</option>`;
        dropdown.innerHTML += option;
    });
});

// Create PO
function createPO() {
    let vendorId = document.getElementById("vendors").value;
    let amount = document.getElementById("amount").value;

    //  Check values first
    if (!vendorId || !amount) {
        alert("Please fill all fields");
        return;
    }

    fetch("http://127.0.0.1:8000/purchase-order", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            reference: "PO123",
            vendor_id: Number(vendorId),   //  FIX
            amount: Number(amount)         //  FIX
        })
    })
    .then(res => res.json())
    .then(data => {
        console.log(data); // debug
        alert("Total with tax: " + data.total_with_tax);
    })
    .catch(err => console.error(err));
}