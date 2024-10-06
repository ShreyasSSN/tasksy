const pointsInput = document.getElementById('id_app_points');
const submitButton = document.getElementById('submit-button');

const toggleButton = () => {
    if (pointsInput.value.trim() !== '' && parseInt(pointsInput.value, 10) !== 0) {
        submitButton.style.display = 'inline';
    } else {
        submitButton.style.display = 'none';
    }
}

pointsInput.addEventListener('input', toggleButton);
toggleButton();