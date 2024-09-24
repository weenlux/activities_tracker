<<<<<<< HEAD
document.getElementById("activityForm").addEventListener("submit", function(e) {
    e.preventDefault();

    const formData = {
        date: document.getElementById('date').value,
        activity: document.getElementById('activity').value,
        duration: document.getElementById('duration').value
    };

    fetch("/save-activity", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
    }).then(response => {
        if (response.ok) {
            alert("Activity saved!");
        } else {
            alert("Failed to save activity.");
        }
    });
});

document.getElementById("exportCSV").addEventListener("click", function() {
    window.location.href = "/export-csv";
=======
document.getElementById("activityForm").addEventListener("submit", function(e) {
    e.preventDefault();

    const formData = {
        date: document.getElementById('date').value,
        activity: document.getElementById('activity').value,
        duration: document.getElementById('duration').value
    };

    fetch("/save-activity", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
    }).then(response => {
        if (response.ok) {
            alert("Activity saved!");
        } else {
            alert("Failed to save activity.");
        }
    });
});

document.getElementById("exportCSV").addEventListener("click", function() {
    window.location.href = "/export-csv";
>>>>>>> e3c23922c2c48dc518a07a3d281c73c99ea5c308
});