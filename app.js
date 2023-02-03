const form = document.querySelector('form');
form.addEventListener('submit', e => {
  e.preventDefault();
  const formData = new FormData(form);
  const data = {};
  formData.forEach((value, key) => {
    data[key] = value;
  });
  // fetch('/predict', {
  fetch('http://localhost:5000/predict', {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(response => response.json())
  .then(data => {
    // Aquí puedes procesar la respuesta del servidor
  });
});

