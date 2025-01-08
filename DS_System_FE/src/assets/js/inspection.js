document.addEventListener("DOMContentLoaded", () => {
    const appointmentTypeInputs = document.querySelectorAll('input[name="appointment-type"]');
    const personalFields = document.getElementById("personal-fields");
    const businessFields = document.getElementById("business-fields");

    appointmentTypeInputs.forEach((input) => {
        input.addEventListener("change", () => {
            if (input.value === "personal") {
                personalFields.style.display = "block";
                businessFields.style.display = "none";
            } else if (input.value === "business") {
                personalFields.style.display = "none";
                businessFields.style.display = "block";
            }
        });
    });
});