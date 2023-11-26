const urlDaPagina = window.location.href;
const id = urlDaPagina.match(/\/(\d+)(?:#|$)/)[1];

const eventoButtonTable = await fetch(`http://127.0.0.1:5000/project_students?project_id=${id}&user_accepted=False`, {
        method: 'GET',
      }).then(response => {
        if (response.ok) {
          response.json().then((data) => {
            data.forEach((aluno) => {
              aceitarAluno(`aceitar${aluno.id}`, aluno.id);
              rejeitarAluno(`rejeitar${aluno.id}`, aluno.id);
            })
        })
    }})

function aceitarAluno(idHTML, idAluno){
  let button = document.getElementById(idHTML);
  console.log(button)
  button.addEventListener("click", (e) => {
    e.preventDefault();

    fetch(`http://127.0.0.1:5000/user/getInscriptionAprove`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      "id_project": id,
      "id_user": idAluno
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
        }).then(() => {
          location.reload();
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
  })
}

function rejeitarAluno(idHTML, idAluno){
  let button = document.getElementById(idHTML);
  console.log(button)
  button.addEventListener("click", (e) => {
    e.preventDefault();

    fetch(`http://127.0.0.1:5000/user/getInscriptionRefused`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      "id_project": id,
      "id_user": idAluno
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
        }).then(() => {
          location.reload();
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
  })
}