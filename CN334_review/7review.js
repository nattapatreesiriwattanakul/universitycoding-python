document.getElementById("registerForm").addEventListener("submit", function(event) {
    let fullname = document.getElementById("fullname").value.trim();
    let email = document.getElementById("email").value.trim();
    let phone = document.getElementById("phone").value;
    let dob = document.getElementById("dob").value;
    let club = document.getElementById("club").value;
    let terms = document.getElementById("terms").checked;

    if (!fullname || !email || !phone || !dob || !club || !terms) {
        alert("กรุณากรอกข้อมูลให้ครบถ้วนและยอมรับเงื่อนไข");
        event.preventDefault();
    }
});

const express = require("express");
const app = express();
const bodyParser = require("body-parser");

app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static(__dirname));

app.post("/submit-form", (req, res) => { //ไม่ออกสอบเรื่องrouting ให้ข้อมูลเป็นแบบอื่นแทน
    res.send(`<h2>ข้อมูลที่ส่งมา:</h2>
        <p>ชื่อ: ${req.body.fullname}</p>
        <p>อีเมล: ${req.body.email}</p>
        <p>เบอร์โทร: ${req.body.phone}</p>
        <p>วันเกิด: ${req.body.dob}</p>
        <p>ชมรมที่เลือก: ${req.body.club}</p>`);
});

app.listen(3000, () => console.log("Server running on port 3000"));
