function calculateBMI() {
    let name = document.getElementById("name").value.trim();
    let weight = document.getElementById("weight").value.trim();
    let feet = document.getElementById("feet").value.trim();
    let inches = document.getElementById("inches").value.trim();

    if (!name || !weight || !feet || !inches) {
        alert("Please fill in all fields!");
        return;
        // document.getElementById("result").innerHTML = "Please fill in all fields!";
        // return;
    }

    fetch('/calculate', {
        method: 'POST',
        body: new URLSearchParams({
            'name': name,
            'weight': weight,
            'feet': feet,
            'inches': inches
        }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerHTML = '';
        if (data.error) {
            document.getElementById("result").innerHTML = data.error;
        } else {
            document.getElementById("result").innerHTML = 
                `${data.name}, your BMI is ${data.bmi}. You are ${data.category}.`;
        }
    });
}


function clearAll() {
    document.getElementById("name").value = "";
    document.getElementById("weight").value = "";
    document.getElementById("feet").value = "";
    document.getElementById("inches").value = "";
    document.getElementById("result").innerHTML = "";
}
