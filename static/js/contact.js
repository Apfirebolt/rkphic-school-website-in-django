document.querySelector('#contact-form').addEventListener('submit', function(e) {
    e.preventDefault();

    let name = document.querySelector('#name').value;
    let email = document.querySelector('#email').value;
    let subject = document.querySelector('#subject').value;
    let message = document.querySelector('#message').value;

    let payload = {
       sender_name: name,
       sender_email: email,
       subject,
       message
    }
    function getCookie(name){
        let pattern = RegExp(name + "=.[^;]*")
        let matched = document.cookie.match(pattern)
        if(matched){
            let cookie = matched[0].split('=')
            return cookie[1]
        }
        return false
    }
    let csrftoken = getCookie('csrftoken');

    fetch('https://rkphic.herokuapp.com/api/messages', {
        method: 'POST',
          headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            "X-CSRFToken": csrftoken
          },
          body: JSON.stringify(payload)
    }).then(res => res.json())
      .then(res => console.log(res));
    });
