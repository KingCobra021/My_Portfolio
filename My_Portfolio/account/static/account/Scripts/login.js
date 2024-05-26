document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById("loginForm");
    const loginBtn = document.getElementById("loginBtn");
    const otpForm = document.getElementById("otpForm");
    const otpBtn = document.getElementById("otpBtn");

    loginBtn.addEventListener("click", function () {
        const formData = new FormData(loginForm);
        fetch("/login/", {
            method: "POST",
            headers: {
                "X-CSRFToken": formData.get("csrfmiddlewaretoken")
            },
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Hide login form and show OTP form
                loginForm.style.display = "none";
                otpForm.style.display = "block";
            } else {
                // Display errors
                const errorDiv = document.getElementById("valid_email");
                errorDiv.innerHTML = data.errors;
            }
        });
    });

    otpBtn.addEventListener("click", function () {
        const formData = new FormData(otpForm);
        fetch("/otp-verify/", {
            method: "POST",
            headers: {
                "X-CSRFToken": formData.get("csrfmiddlewaretoken")
            },
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Redirect to home or desired page after successful OTP verification
                window.location.href = "/";
            } else {
                // Display errors
                alert(data.errors);
            }
        });
    });
});
