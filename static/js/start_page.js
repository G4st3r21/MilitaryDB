const textContainer = document.querySelector('.text-container');

// Сначала воспроизведите анимацию букв
textContainer.classList.remove('paused');

// Остановите анимацию букв и добавьте задержку после того, как анимация завершится
textContainer.classList.add('paused');
setTimeout(() => {
  textContainer.classList.remove('paused');
  textContainer.classList.add('running');
}, 2000);