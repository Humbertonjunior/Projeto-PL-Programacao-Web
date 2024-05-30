const controls = document.querySelectorAll(".control");
let currentItem = 0;
const items = document.querySelectorAll(".item");
const maxItems = items.length;

function nextItem() {
  currentItem = (currentItem + 1) % maxItems;
  updateCarousel();
}

function updateCarousel() {
  items.forEach((item) => item.classList.remove("current-item"));
  items[currentItem].scrollIntoView({
    behavior: "smooth",
    inline: "center"
  });
  items[currentItem].classList.add("current-item");
}

// Adiciona um ouvinte de evento de clique para mudar a imagem quando clicar nas setas
controls.forEach((control) => {
  control.addEventListener("click", (e) => {
    e.preventDefault();
    const isLeft = e.target.classList.contains("arrow-left");
    if (isLeft) {
      currentItem = (currentItem - 1 + maxItems) % maxItems;
    } else {
      currentItem = (currentItem + 1) % maxItems;
    }
    updateCarousel();
  });
});
