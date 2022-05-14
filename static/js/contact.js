document.querySelector('#contact-form').addEventListener('submit', function(e) {
    e.preventDefault();

    let name = document.getElementById('name"]');
    let email = document.getElementById('email"]');
    let subject = document.getElementById('subject"]');
    let message = document.getElementById('message"]');
    console.log('Prevented submit ', name, email, subject, message);
});