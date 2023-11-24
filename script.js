document.addEventListener("DOMContentLoaded", function () {
  var header = document.querySelector("header");
  var nav = document.querySelector("nav");

  window.addEventListener("scroll", function () {
    var scrollPosition = window.scrollY;

    if (scrollPosition > 100) {
      header.classList.add("scrolled");
      nav.classList.add("scrolled");
    } else {
      header.classList.remove("scrolled");
      nav.classList.remove("scrolled");
    }
  });
});


document.addEventListener("DOMContentLoaded", function () {
  var header = document.querySelector("header");
  var nav = document.querySelector("nav");

  window.addEventListener("scroll", function () {
    var scrollPosition = window.scrollY;

    if (scrollPosition > 100) {
      header.classList.add("scrolled");
      nav.classList.add("scrolled");
    } else {
      header.classList.remove("scrolled");
      nav.classList.remove("scrolled");
    }
  });
});


function submitForm() {

  var name = document.getElementById('name').value;
  var email = document.getElementById('email').value;


  if (name !== '' && email !== '') {

    showMessage('Agradecemos o contato! Por favor, preencha com seus dados!');


    clearForm();
  } else {
    showMessage('Por favor, preencha todos os campos!');
  }
}

function showMessage(message) {

  var messageElement = document.createElement('p');
  messageElement.textContent = message;


  var contactSection = document.querySelector('.contact-section');
  contactSection.appendChild(messageElement);
}

function clearForm() {
  document.getElementById('name').value = '';
  document.getElementById('email').value = '';
  document.getElementById('phone').value = '';
  document.getElementById('message').value = '';
}
