const items = document.querySelectorAll('.sourate-item');
items.forEach(item => {
  item.addEventListener('click', () => {
    const name = item.textContent;
    fetch(`http://localhost:5000/sourate/${name}`)
      .then(response => {
        if (response.ok) {
          // Rediriger vers la page correspondante
          window.location.href = `http://localhost:5000/sourate/${name}`;
        } else {
          alert('Une erreur est survenue. Veuillez réessayer.');
        }
      })
  });
});