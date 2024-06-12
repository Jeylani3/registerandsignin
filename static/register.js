document.getElementById('registerButton').addEventListener('click', function(event) {
    event.preventDefault();  // Prevent default form submission
    register();
  });
  
  function register() {
    const formData = {
      username: document.getElementById('username').value,
      password: document.getElementById('password').value,
      confirm_password: document.getElementById('confirm_password').value
    };
  
    if (formData.password !== formData.confirm_password) {
      alert("Passwords don't match!");
      return;
    }
  
    fetch('http://127.0.0.1:8000/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    })
    .then(response => response.json())
    // .then(data => console.log(data))
    .then(data => document.getElementById('response').innerText = data.message)
    .catch(error => console.error('Error:', error));
  }