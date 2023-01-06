<script>
  // Slider de imágenes
  var slider = document.getElementById("slider");
  var slides = slider.getElementsByClassName("slide");
  var currentSlide = 0;
  setInterval(showNextSlide, 3000); // Muestra el siguiente slide cada 3 segundos

  function showNextSlide() {
    // Oculta el slide actual
    slides[currentSlide].style.display = "none";

    // Incrementa el slide actual
    currentSlide = (currentSlide + 1) % slides.length;

    // Muestra el slide siguiente
    slides[currentSlide].style.display = "block";
  }

  // Formulario dinámico
  var formulario = document.getElementById("formulario");
  formulario.addEventListener("input", actualizaFormulario);

  function actualizaFormulario() {
    // Recupera el valor del campo "nombre"
    var nombre = formulario.elements.nombre.value;

    // Muestra un mensaje de bienvenida si el campo "nombre" no está vacío
    if (nombre.trim() != "") {
      console.log("Bienvenido, " + nombre + "!");
    }
  }
</script>
