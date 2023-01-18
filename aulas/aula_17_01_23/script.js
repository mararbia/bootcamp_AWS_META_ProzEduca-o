// ---------- FUNÇÕES GERAIS -------------- //
function togglePopup(input, label) {
  // Mostrar popup de campo obrigatório
  input.addEventListener("focus", () => {
    label.classList.add("required-popup");
  });

  // Ocultar popup de campo obrigatório
  input.addEventListener("blur", () => {
    label.classList.remove("required-popup");
  });
}

function estilizarInputCorreto(input, helper) {
  helper.classList.remove("visible");
  input.classList.remove("error");
  input.classList.add("correct");
}

function estilizarInputIncorreto(input, helper) {
  helper.classList.add("visible");
  input.classList.add("error");
  input.classList.remove("correct");
}

// ---------- VALIDAÇÃO USERNAME ---------- //
let usernameInput = document.getElementById("username");
let usernameLabel = document.querySelector('label[for="username"]');
let usernameHelper = document.getElementById("username-helper");

togglePopup(usernameInput, usernameLabel)

// Validar valor do input
usernameInput.addEventListener("change", (e)=> {
  let valor = e.target.value

  if(valor.length < 3){
    // Adicionar estilos dinâmicos se o valor tiver menos de 3 caracteres
    usernameHelper.innerText = "Seu username precisa ter 3 ou mais caracteres";
    estilizarInputIncorreto(usernameInput, usernameHelper)
  } else {
    // Adicionar estilos dinâmicos se o valor estiver correto
    estilizarInputCorreto(usernameInput, usernameHelper);
  }
})

// ---------- VALIDAÇÃO EMAIL ---------- //
let emailInput = document.getElementById("email");
let emailLabel = document.querySelector('label[for="email"]');
let emailHelper = document.getElementById("email-helper");

togglePopup(emailInput, emailLabel)

// Validar valor do input
emailInput.addEventListener("change", (e)=> {
  let valor = e.target.value

  if(valor.includes("@") && valor.includes(".com")){
    // Adicionar estilos dinâmicos se o valor estiver correto
    estilizarInputCorreto(emailInput, emailHelper);
  } else {
    // Adicionar estilos dinâmicos se o valor tiver menos de 3 caracteres
    emailHelper.innerText = "Precisa inserir um email válido";
    estilizarInputIncorreto(emailInput, emailHelper);
  }
})

// Validação senha
let inputSenha = document.getElementById("senha");
let labelSenha = document.querySelector('label[for=senha]');
let msgErrorSenha = document.getElementById("senha-helper");

// Events Input
inputSenha.addEventListener("blur", (e) =>{
  let valorDaSenha = e.target.value;
 
  if(valorDaSenha.length > 0) {
    estilizarInputCorreto(inputSenha, msgErrorSenha);
  } else {
    msgErrorSenha.innerText = "É preciso informar uma senha";
    estilizarInputIncorreto(inputSenha, msgErrorSenha);
  }  
})

// Validação confirmar senha
let inputConfirmarSenha = document.getElementById("confirma-senha");
let labelConfirmarSenha = document.getElementById("confirma-senha");
let msgErrorConfirmaSenha = document.getElementById("confirma-senha-helper");

inputConfirmarSenha.addEventListener("blur", (e) => {
  let confirmaSenha = e.target.value;

  if (confirmaSenha === inputSenha.value) {
    estilizarInputCorreto(inputConfirmarSenha, msgErrorConfirmaSenha);
  } else {
    msgErrorConfirmaSenha.innerText = "Favor inserir a mesma senha";
    estilizarInputIncorreto(inputConfirmarSenha, msgErrorConfirmaSenha);
  }
});