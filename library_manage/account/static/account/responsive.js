const form = document.querySelector('form');
form.addEventListener('submit', (event) => {
    

    const email = document.getElementById('email').value;
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!emailPattern.test(email)) {
        // Display error message for invalid email format
        const errorElement = document.getElementById('emailError');
        errorElement.textContent = 'Invalid email format';
        errorElement.style.display = 'block';

        return;
    }

});

function validateForm() {
    var checkbox = document.getElementById('id_is_student');
    var checkboxError = document.getElementById('checkbox-error');

    if (!checkbox.checked) {
        checkboxError.textContent = "You must agree to the terms and conditions.";
        return false;
    }

    return true;
}

// Event listener for form submission
document.getElementById('register-form').addEventListener('submit', function(event) {
    if (!validateForm()) {
        event.preventDefault(); // Prevent form submission if validation fails
    }
});
