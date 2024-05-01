const modalBackground = document.getElementById('modal-background');
const closeButton = document.getElementById('close-button');
const courseButtons = document.getElementsByClassName('course-button');

function openModal() {
    modalBackground.style.display = 'flex';
}

function closeModal() {
    modalBackground.style.display = 'none';
}

for (let i = 0; i < courseButtons.length; i++) {
    courseButtons[i].addEventListener('click', openModal);
}

closeButton.addEventListener('click', closeModal);

window.addEventListener('click', (event) => {
    if (event.target === modalBackground) {
        closeModal();
    }
});