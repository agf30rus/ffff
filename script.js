function showScreen(screenId) {
    document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
    document.getElementById('screen-' + screenId).classList.add('active');
}

// Инициализация Telegram WebApp
const tg = window.Telegram.WebApp;
tg.ready();
