import { getCookie } from "./utilites/cookie";

var email = getCookie();
var extend = email.split("@")

var navbarProfessor = document.getElementById('navbar_professor');
var navbarStudent = document.getElementById('navbar-container');


if (extend[1] == "academico.ifpb.edu.br") {
    navbarStudent.style.display = 'inline-block';
    navbarProfessor.style.display = 'none';
} else if (extend[0] == "ifpb.edu.br") {
    navbarStudent.style.display = 'none';
    navbarProfessor.style.display ='inline-block';
}
