const button = document.getElementById("editar-projeto");

button.addEventListener("click", (e)=>{
    e.preventDefault();
    window.location = "http://127.0.0.1:5000/projects/update";
})