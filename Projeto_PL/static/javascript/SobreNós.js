var password = document.getElementById("senha")
  , confirm_password = document.getElementById("Confirmarsenha");

function validatePassword(){
  if(password.value != confirm_password.value) {
    confirm_password.setCustomValidity("As senhas não batem");
  } else {
    confirm_password.setCustomValidity('');
  }
}

password.onchange = validatePassword;
confirm_password.onkeyup = validatePassword;
function formatar(mascara, documento) {
    let i = documento.value.length;
    let saida = '#';
    let texto = mascara.substring(i);
    while (texto.substring(0, 1) != saida && texto.length ) {
      documento.value += texto.substring(0, 1);
      i++;
      texto = mascara.substring(i);
    }
  }
  function redirect() {
    var selectBox = document.getElementById("menuOptions");
    var selectedValue = selectBox.options[selectBox.selectedIndex].value;
    if (selectedValue === "login") {
      window.location.href = 'pagina_de_login.html';
    } else if (selectedValue === "inscrever") {
      window.location.href = 'pagina_de_inscricao.html';
    } else if (selectedValue === "sair") {
      window.location.href = 'pagina_de_sair.html';
    }
  }
