const eventoButtonTable = await fetch(`http://127.0.0.1:5000/user/${professor}`, {
        method: 'GET',
      }).then(response => {
        if (response.ok) {
          response.json().then((data) => {
            document.getElementById("professor_name").textContent = `Servidor: ${data.name}`
      })
}})