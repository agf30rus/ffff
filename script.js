const tg = window.Telegram.WebApp;

// Инициализация
tg.ready();
tg.expand();
tg.setHeaderColor('#000000');
tg.setBackgroundColor('#000000');

function showScreen(screenId) {
    document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
    document.getElementById('screen-' + screenId).classList.add('active');
}

// Пример переключения по клику на кнопку устройства
document.querySelectorAll('.device-btn').forEach(btn => {
    btn.onclick = () => showScreen(2);
});
