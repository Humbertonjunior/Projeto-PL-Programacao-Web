function redirect() {
    var selectBox = document.getElementById("menuOptions");
    var selectedValue = selectBox.options[selectBox.selectedIndex].value;
    if (selectedValue === "perfil") {
      window.location.href = 'pagina_de_perfil.html';
    } else if (selectedValue === "login") {
      window.location.href = 'pagina_de_login.html';
    } else if (selectedValue === "inscrever") {
      window.location.href = 'pagina_de_inscricao.html';
    } else if (selectedValue === "sair") {
      window.location.href = 'pagina_de_sair.html';
    }
  }
  