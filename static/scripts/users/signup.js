const button_criar_conta = document.getElementById("signup");

button_criar_conta.addEventListener("click", (e) =>{
  e.preventDefault();

  const password = document.getElementById("password").valeu;
  const confirmPassword = document.getElementById("confirmPassword").valeu;

  if(password === confirmPassword){

    const selectBirth = document.querySelector('#birth');
    const selectTitle = document.querySelector('#title');

    const jsonRegister = {
      "email": document.getElementById("email").valeu,
      "firstname": document.getElementById("firstname").valeu,
      "password": password,
      "gender": document.getElementById("gender").valeu,
      "registration": document.getElementById("registration").valeu,
      "birth": selectBirth.options[selectBirth.selectedIndex].value,
      "title": selectTitle.options[selectTitle.selectedIndex].value,
    }
  
    fetch("127.0.0.1:3000/user/getregister", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(jsonRegister) 
    })
    .then(response => {
      if (!response.ok) {
        Swal.fire({
          icon: "error",
          title: "Oops...",
          text: response.json(),
        });
      }
      Swal.fire({
        position: "center",
        icon: "success",
        title: "Conta criada com sucesso",
        showConfirmButton: false,
        timer: 1000
      });
    })
    .catch(error => {
      Swal.fire({
        icon: "error",
        title: "Oops...",
        text: error,
      });
    });

  }else{
    Swal.fire({
      icon: "error",
      title: "Oops...",
      text: error,
    });
  }

});