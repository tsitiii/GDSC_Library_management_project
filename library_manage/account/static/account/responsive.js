

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

const greeting = (name) => {

    console.log("hello")

    const greet = document.createElement('div');
    greet.textContent = `Hello ${name} !!!`
    return greet
}
const welcome = document.getElementsByTagName('h1')[0]
welcome.appendChild(greeting('zion the mean😊🎉'))

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