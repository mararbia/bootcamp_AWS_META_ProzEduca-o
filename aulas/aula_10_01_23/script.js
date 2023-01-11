const linkPerfil = document.getElementById("link-perfil");
const navPerfil = document.getElementById("nav-perfil");
const linkPerfilDados = document.getElementById("link-perfil-dados");
linkPerfil.addEventListener("mouseover", () => {
    navPerfil.style.display = "block";
});

window.addEventListener("keydown", (event) => {
    console.log(event.key);
    console.log(event.code);
    
    if (navPerfil.style.display == "block"){
        // window.open(linkPerfilDados, '');
        //ou
        linkPerfil.click()
    } else if(event.code == "Digit1"){
        navPerfil.style.display = "block";
    } else if(event.code == "Escape"){
        navPerfil.style.display = "none";
    } 
});