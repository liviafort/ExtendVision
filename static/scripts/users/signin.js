const button_criar_conta = document.getElementById("login");

button_criar_conta.addEventListener("click", (e) =>{
  e.preventDefault();
  window.location = "http://127.0.0.1:5000/professor/home";
});