document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('loginButton').addEventListener('click', function(event) {
      event.preventDefault();  // Prevent default form submission
      login();
    });
  });
  
  function login() {
    const formData = {
      username: document.getElementById('username1').value,
      password: document.getElementById('password').value
    };
  
    fetch('http://127.0.0.1:8000/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
         console.log(data)
         const responseElement = document.getElementById('response').innerText = data.message;
        //  responseElement.textContent = JSON.stringify(data["message"]);
        //  responseElement.textContent = data["message"]; 
        })
    .catch(error => console.error('Error:', error));
  }

  