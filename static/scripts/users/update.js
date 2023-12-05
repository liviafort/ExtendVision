const button_update = document.getElementById("update");

button_update.addEventListener("click", (e) =>{
  e.preventDefault();
    const selectGender = document.querySelector('#gender');

    const jsonRegister = {
      "email": document.getElementById("email").value,
      "name": document.getElementById("name").value,
      "gender": selectGender.options[selectGender.selectedIndex].value,
      "registration": document.getElementById("matricula").value,
      "birth": document.getElementById("birth").value,
    }
  
    fetch("http://127.0.0.1:5000/user/update", {
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

  });