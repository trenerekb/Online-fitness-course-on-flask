
// UPLOAD AVATAR
btnSend = document.getElementById('btn-send-photo-avatar')
btnFile = document.getElementById('file')
classBtnFile = document.querySelector('.inline-option-btn')

btnFile.onclick = () => {
        btnSend.style.display = 'inline-block';
        classBtnFile.style.display = 'none';
}
