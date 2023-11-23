
  function changeColor(element) {
    // Remove a classe 'active' de todos os links
    var links = document.querySelectorAll('nav a');
    links.forEach(function(link) {
      link.classList.remove('active');
    });
  
    // Adiciona a classe 'active' ao link clicado
    element.classList.add('active');
  }
  
  function changeColorWithDelay(element) {
    // Adiciona a classe 'active' com delay
    setTimeout(function() {
      changeColor(element);
    }, 500); // Tempo em milissegundos (neste caso, 0,5 segundos)
  }
  