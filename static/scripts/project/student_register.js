const button_inscrever = document.getElementById("inscrever");

button_inscrever.addEventListener("click", (e) =>{
  e.preventDefault();
  fetch("http://127.0.0.1:5000/user/getregister", {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(id) 
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
  
});
