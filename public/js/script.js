// Основной JavaScript для сайта

document.addEventListener('DOMContentLoaded', function() {

    // Мобильное меню
    const menuToggle = document.querySelector('.menu-toggle');
    const mainNav = document.querySelector('.main-nav');

    if (menuToggle && mainNav) {
        menuToggle.addEventListener('click', function() {
            mainNav.classList.toggle('active');
            menuToggle.innerHTML = mainNav.classList.contains('active')
                ? '<i class="fas fa-times"></i>'
                : '<i class="fas fa-bars"></i>';
        });

        // Закрытие меню при клике на ссылку
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                mainNav.classList.remove('active');
                menuToggle.innerHTML = '<i class="fas fa-bars"></i>';
            });
        });
    }

    // Плавная прокрутка для якорных ссылок
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');

            if (href !== '#' && href.startsWith('#')) {
                e.preventDefault();
                const targetElement = document.querySelector(href);

                if (targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop - 80,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });

    // Кнопки "Прочитать отрывок" на странице историй
    const readStoryButtons = document.querySelectorAll('.btn-read-story');
    const storyModal = document.getElementById('storyModal');
    const modalClose = document.querySelector('.modal-close');
    const modalContent = document.getElementById('modalStoryContent');

    // Отрывки для каждой истории
    const storyExcerpts = [
        `<h2>Ящик с ушами</h2>
        <p>На большом белом корабле, который плыл к далёким тёплым островам, случилась странная история. Каждое утро пропадали бананы из кают-компании...</p>
        <p>А из картонного ящика, который стоял в углу каюты, иногда доносилось странное шуршание. И если прислушаться очень внимательно, можно было услышать тихое-тихое посапывание...</p>`,

        `<h2>Пингвин-моряк</h2>
        <p>В самом холодном порту Антарктики жил пингвин по имени Пинги. Все пингвины вокруг ныряли за рыбой, грелись на льдинах и воспитывали птенцов. А Пинги мечтал стать моряком...</p>
        <p>"Пингвины не бывают моряками!" - говорили ему друзья. "У нас ласты, а у моряков руки!"</p>`,

        `<h2>Воздушный говорящий змей</h2>
        <p>В один ветреный день мальчик Вася запускал во дворе воздушного змея. Змей был красивый, разноцветный, с длинным хвостом...</p>
        <p>И вдруг змей сказал: "Привет! Мне нравится летать!" Вася так удивился, что чуть не выпустил верёвку из рук...</p>`,

        `<h2>Тайна знаков препинания</h2>
        <p>Однажды ночью, когда все спали, из книжки вылезла Точка. За ней - Запятая, потом - Восклицательный знак...</p>
        <p>"Надоело нам стоять на одном месте!" - сказала Запятая. "Давайте устроим праздник!" - воскликнул Восклицательный знак...</p>`,

        `<h2>Пятая сказка</h2>
        <p>Эта история началась с маленького секрета. Не такого, который нельзя рассказывать, а такого, который хочется беречь, как самое дорогое сокровище...</p>
        <p>И если вы будете очень внимательны, то, возможно, этот секрет откроется и вам...</p>`
    ];

    if (readStoryButtons.length > 0) {
        readStoryButtons.forEach((button, index) => {
            button.addEventListener('click', function() {
                const storyIndex = this.getAttribute('data-story') - 1;
                modalContent.innerHTML = storyExcerpts[storyIndex];
                storyModal.classList.add('active');
                document.body.style.overflow = 'hidden';
            });
        });
    }

    // Закрытие модального окна
    if (modalClose && storyModal) {
        modalClose.addEventListener('click', function() {
            storyModal.classList.remove('active');
            document.body.style.overflow = 'auto';
        });

        // Закрытие по клику вне окна
        storyModal.addEventListener('click', function(e) {
            if (e.target === storyModal) {
                storyModal.classList.remove('active');
                document.body.style.overflow = 'auto';
            }
        });

        // Закрытие по Escape
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && storyModal.classList.contains('active')) {
                storyModal.classList.remove('active');
                document.body.style.overflow = 'auto';
            }
        });
    }

    // Анимация появления элементов при скролле
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animated');
            }
        });
    }, observerOptions);

    // Наблюдаем за элементами для анимации
    document.querySelectorAll('.story-card, .quote-card, .character-item').forEach(el => {
        observer.observe(el);
    });

    // Кнопка "Читать" в шапке
    const readButtons = document.querySelectorAll('.btn-read, .nav-link.btn-read');
    readButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (this.getAttribute('href') === '#read') {
                e.preventDefault();
                const ctaSection = document.getElementById('read');
                if (ctaSection) {
                    window.scrollTo({
                        top: ctaSection.offsetTop - 80,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });

    // Добавляем год в подвал
    const yearElement = document.querySelector('.current-year');
    if (yearElement) {
        yearElement.textContent = new Date().getFullYear();
    }
});