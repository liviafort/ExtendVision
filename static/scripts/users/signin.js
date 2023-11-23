const button_login = document.getElementById("login");
const button_criar_conta = document.getElementById("registrar");

button_criar_conta.addEventListener("click", (e) =>{
  e.preventDefault();
  window.location = "http://127.0.0.1:5000/register"
})

button_login.addEventListener("click", (e) =>{
  e.preventDefault();

  const jsonLogin = {
    "email": document.getElementById("email").value,
    "password": document.getElementById("password").value,
  }

  console.log(jsonLogin)

  fetch("http://127.0.0.1:5000/user/getlogin", {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(jsonLogin) 
  })
  .then(response => {
    if(response.ok){
      response.json().then((data) => {
        if(data.user_type === "teacher"){
          window.location = "http://127.0.0.1:5000/professor/home";
        }else if(data.user_type === "student"){
          window.location = "http://127.0.0.1:5000/student/home";
        }
      })
    }else{
      response.json().then((data) => {
        Swal.fire({
          position: "center",
          icon: "error",
          title: "Oops...",
          text: data.error,
        });
      })
    }
  })
  .catch(error => {
    Swal.fire({
      position: "center",
      icon: "error",
      title: "Oops...",
      text: error,
    });
  });
});