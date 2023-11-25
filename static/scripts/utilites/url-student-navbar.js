document.addEventListener("DOMContentLoaded", async (e) => {
    e.preventDefault()
    let user;
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith("user=")) {
            user = cookie.substring("user=".length);
            break;
        }
    }
    
    user = 1;
    
    const perfil = document.getElementById("perfil");
    const profile = document.getElementById("profile");
    const meus_projetos = document.getElementById("meus_projetos");
    const minhas_inscricoes = document.getElementById("minhas_inscricoes");

    profile.href = `http://127.0.0.1:5000/student/profile`;
    perfil.href = `http://127.0.0.1:5000/student/profile`;
    meus_projetos.href = `http://127.0.0.1:5000/student/account/myProjects/${user}`;
    minhas_inscricoes.href = `http://127.0.0.1:5000/student/account/myProjects/${user}`;
})
