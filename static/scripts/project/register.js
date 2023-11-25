import { getCookie } from "../utilites/cookie";

//---------ADICIONANDO OPTION AO SELECT ------------//
document.addEventListener("DOMContentLoaded", async (e) => {
  e.preventDefault()
  let select = document.getElementById("area");
  
  fetch("http://127.0.0.1:5000/field", {
      method: 'GET',
    })
    .then(response => {
      if (response.ok) {
        response.json().then((data) => {
          data.forEach(function(field) {
            let option = document.createElement("option");
            option.value = field.field;
            option.text = field.field;
            select.appendChild(option);
          })
      })
    }})
})

//--------------CRIAÇÃO DE PROJETO ----------------//

const button_register_projeto = document.getElementById("registerProjeto");

button_register_projeto.addEventListener("click", (e) =>{
  e.preventDefault();

  const email = getCookie();
  const titulo = document.getElementById("titulo").value;
  const tema = document.getElementById("tema").value;
  const selectArea = document.querySelector('#area');
  const area = selectArea.options[selectArea.selectedIndex].value;
  const descricao = document.getElementById("descricao").value;
  const carga = document.getElementById("carga").value;
  const vagas = document.getElementById("vagas").value;
  const inicioProjeto = document.getElementById("inicioProjeto").value;
  const terminoProjeto = document.getElementById("terminoProjeto").value;
  const inicioInscricao = document.getElementById("inicioInscricao").value;
  const terminoInscricao = document.getElementById("terminoInscricao").value;
  const valor = document.getElementById("valor").value;

  const jsonRegister = {
    "email": email,
    "title": titulo,
    "theme": tema,
    "area": area,
    "description": descricao,
    "workload": parseInt(carga),
    "available_spots": parseInt(vagas),
    "begin_date": inicioProjeto,
    "end_date": terminoProjeto,
    "register_begin": inicioInscricao,
    "register_end": terminoInscricao,
    "scholarship": parseInt(valor)
  }

  fetch("http://127.0.0.1:5000/user/getproject", {
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
        }).then(() => {
          window.location = "http://127.0.0.1:5000/professor/home"
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