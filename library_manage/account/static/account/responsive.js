

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

