const button_criar_conta = document.getElementById("login");

button_criar_conta.addEventListener("click", (e) =>{
  e.preventDefault();

  const jsonLogin = {
    "email": document.getElementById("email").valeu,
    "password": document.getElementById("password").valeu,
  }

  fetch("127.0.0.1:3000/user/getlogin", {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(jsonLogin) 
  })
  .then(response => {
    if (!response.ok) {
      Swal.fire({
        icon: "error",
        title: "Oops...",
        text: response.json(),
      });
    }
  })
  .catch(error => {
    Swal.fire({
      icon: "error",
      title: "Oops...",
      text: error,
    });
  });
});