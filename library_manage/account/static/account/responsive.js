

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