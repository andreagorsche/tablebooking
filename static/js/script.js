// Get references to the menu cards
const breakfastCard = document.getElementById('breakfast-card');
const lunchCard = document.getElementById('lunch-card');
const dinnerCard = document.getElementById('dinner-card');

// Function to toggle the flipped class on the card
function toggleFlip(card) {
  card.classList.toggle('flipped');
}

// Add event listeners to trigger the flip animation on hover
breakfastCard.addEventListener('mouseenter', () => toggleFlip(breakfastCard));
breakfastCard.addEventListener('mouseleave', () => toggleFlip(breakfastCard));

lunchCard.addEventListener('mouseenter', () => toggleFlip(lunchCard));
lunchCard.addEventListener('mouseleave', () => toggleFlip(lunchCard));

dinnerCard.addEventListener('mouseenter', () => toggleFlip(dinnerCard));
dinnerCard.addEventListener('mouseleave', () => toggleFlip(dinnerCard));
