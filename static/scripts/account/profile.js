document.addEventListener("DOMContentLoaded", async (e) => {
  e.preventDefault()

  const selectElement1 = document.querySelector(`#gender`);
  for (let j = 0; j < selectElement1.options.length; j++) {
    if (selectElement1.options[j].value === genero) {
      selectElement1.selectedIndex = j;
      break;
    }
  }
})