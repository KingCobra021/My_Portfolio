document.addEventListener("DOMContentLoaded", function () {
    const emailInput = document.getElementById("id_email");
    const passwordInput = document.getElementById("id_password");

    emailInput.addEventListener("focus", function () {
        emailInput.style.borderBottomColor = "#2772da";
        emailInput.style.color = "#ff5200";
    });

    emailInput.addEventListener("blur", function () {
        emailInput.style.borderBottomColor = "#ff5200";
        emailInput.style.color = "#2772da";
    });

    passwordInput.addEventListener("focus", function () {
        passwordInput.style.borderBottomColor = "#2772da";
        passwordInput.style.color = "#ff5200";
    });

    passwordInput.addEventListener("blur", function () {
        passwordInput.style.borderBottomColor = "#ff5200";
        passwordInput.style.color = "#2772da";
    });
});
