const button_criar_conta = document.getElementById("signup");

button_criar_conta.addEventListener("click", (e) =>{
  e.preventDefault();

  const password = document.getElementById("password").value;
  const confirmPassword = document.getElementById("confirmPassword").value;

  if(password === confirmPassword){

    const selectGender = document.querySelector('#gender');

    const jsonRegister = {
      "email": document.getElementById("email").value,
      "name": document.getElementById("firstname").value,
      "password": password,
      "gender": selectGender.options[selectGender.selectedIndex].value,
      "registration": document.getElementById("registration").value,
      "birth": document.getElementById("birth").value,
    }
  
    console.log(jsonRegister)
    fetch("http://127.0.0.1:5000/user/getregister", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(jsonRegister) 
    })
    .then(response => {
      if (response.ok) {
        response.json().then((data) => {
          Swal.fire({
            position: "center",
            icon: "success",
            title: data.works,
            showConfirmButton: false,
            timer: 1500
          }).then(() =>{
              window.location = "http://127.0.0.1:5000/"
          })
        })
      }else{
        response.json().then((data) => {
          Swal.fire({
            icon: "error",
            title: "Oops...",
            text: data.error,
            });
        })

      }
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
      text: "As senhas não coincidem"
    });
  }

});