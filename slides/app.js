const slides = Array.from(document.querySelectorAll(".slide"));
const counter = document.querySelector("#slide-counter");
const title = document.querySelector("#current-title");
const progressFill = document.querySelector("#progress-fill");
const prevButton = document.querySelector("#prev-button");
const nextButton = document.querySelector("#next-button");

let currentIndex = 0;

function clampIndex(index) {
  return Math.min(Math.max(index, 0), slides.length - 1);
}

function updateDeck(index) {
  currentIndex = clampIndex(index);

  slides.forEach((slide, slideIndex) => {
    slide.classList.toggle("is-active", slideIndex === currentIndex);
    slide.setAttribute("aria-hidden", slideIndex === currentIndex ? "false" : "true");
  });

  const currentSlide = slides[currentIndex];
  const total = slides.length;
  const progress = total === 1 ? 100 : (currentIndex / (total - 1)) * 100;

  counter.textContent = `${currentIndex + 1} / ${total}`;
  title.textContent = currentSlide.dataset.title || `Slide ${currentIndex + 1}`;
  progressFill.style.width = `${progress}%`;
  prevButton.disabled = currentIndex === 0;
  nextButton.disabled = currentIndex === total - 1;
}

function step(delta) {
  updateDeck(currentIndex + delta);
}

prevButton.addEventListener("click", () => step(-1));
nextButton.addEventListener("click", () => step(1));

window.addEventListener("keydown", (event) => {
  if (
    event.target instanceof HTMLElement &&
    ["INPUT", "TEXTAREA", "SELECT"].includes(event.target.tagName)
  ) {
    return;
  }

  switch (event.key) {
    case "ArrowRight":
    case "PageDown":
    case " ":
      event.preventDefault();
      step(1);
      break;
    case "ArrowLeft":
    case "PageUp":
      event.preventDefault();
      step(-1);
      break;
    case "Home":
      event.preventDefault();
      updateDeck(0);
      break;
    case "End":
      event.preventDefault();
      updateDeck(slides.length - 1);
      break;
    default:
      break;
  }
});

updateDeck(0);
