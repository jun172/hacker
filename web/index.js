// ハンバーガーメニュー制御
const menuOpenButton = document.getElementById('menu-open-button');
const menuCloseButton = document.getElementById('menu-close-button');
const body = document.body;

menuOpenButton.addEventListener('click', () => {
    body.classList.add('show-mobile-menu');
});

menuCloseButton.addEventListener('click', () => {
    body.classList.remove('show-mobile-menu');
});

// メニュー内リンククリックでも閉じる（任意）
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
        body.classList.remove('show-mobile-menu');
    });
});
