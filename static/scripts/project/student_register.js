import { getUser } from "../utilites/cookie.js";

const button_inscrever = document.getElementById("inscrever");

button_inscrever.addEventListener("click", (e) =>{
  e.preventDefault();

  const urlDaPagina = window.location.href;
  const idProjetc = urlDaPagina.match(/\/(\d+)(?:#|$)/)[1];


  fetch("http://127.0.0.1:5000/user/getInscription", {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      "id_user": parseInt(getUser()),
      "id_project": parseInt(idProjetc)
    }) 
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
  
});
