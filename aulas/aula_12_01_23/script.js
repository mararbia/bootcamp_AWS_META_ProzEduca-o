let usernameInput = document.getElementById("username");
let usernameLabel = document.querySelector('label[for="username');
let usernameHelper = document.getElementById("username-helper");
let emailInput = document.getElementById("email");

// Mostrar popup de campo obrigatório
usernameInput.addEventListener("focus", () => {
  usernameLabel.classList.add("required-popup");
});

// Ocultar popup de campo obrigatório
usernameInput.addEventListener("blur", () => {
  usernameLabel.classList.remove("required-popup");
});

// Valor valor do input
usernameInput.addEventListener("change", (e) => {
  let valueInput = e.target.value;

  if (valueInput.length < 3) {
    usernameInput.classList.add("error");
    usernameHelper.innerHTML =
      "Username inválido! Precisa ser no mínimo 6 caracteres";
      usernameHelper.classList.add("visible");
  } else {
    usernameHelper.classList.remove("visible");
    usernameInput.classList.add("correct");
  }
});

// Evento for email
emailInput.addEventListener("change", (e) => {
    let emailValue = e.target.value;

    if (emailValue.includes("@")){
        emailInput.classList.remove("error");
        emailInput.classList.add("correct");
    } else {
        emailInput.classList.add("error");
    }
})
