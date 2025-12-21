// Обновленный скрипт - упрощаем навигацию

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
                if (window.innerWidth <= 768) {
                    mainNav.classList.remove('active');
                    menuToggle.innerHTML = '<i class="fas fa-bars"></i>';
                }
            });
        });
    }

    // Переключение между категориями
    const categoryLinks = document.querySelectorAll('.category-link');
    const categoryContents = document.querySelectorAll('.category-content');

    categoryLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();

            const targetId = this.getAttribute('href');
            const targetContent = document.querySelector(targetId);

            // Скрываем все содержимое
            categoryContents.forEach(content => {
                content.classList.remove('active');
            });

            // Показываем выбранное содержимое
            if (targetContent) {
                targetContent.classList.add('active');

                // Плавная прокрутка к содержимому
                setTimeout(() => {
                    targetContent.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }, 100);
            }

            // Закрываем мобильное меню если открыто
            if (window.innerWidth <= 768 && mainNav) {
                mainNav.classList.remove('active');
                menuToggle.innerHTML = '<i class="fas fa-bars"></i>';
            }
        });
    });

    // Закрытие содержимого при клике вне его
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.category-link') &&
            !e.target.closest('.category-content')) {
            categoryContents.forEach(content => {
                content.classList.remove('active');
            });
        }
    });

    // Плавная прокрутка для остальных ссылок
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');

            if (href !== '#' && href.startsWith('#') &&
                !href.includes('-content') &&
                !this.classList.contains('category-link')) {
                e.preventDefault();
                const targetElement = document.querySelector(href);

                if (targetElement) {
                    // Закрываем содержимое категорий
                    categoryContents.forEach(content => {
                        content.classList.remove('active');
                    });

                    // Закрываем мобильное меню если открыто
                    if (window.innerWidth <= 768 && mainNav) {
                        mainNav.classList.remove('active');
                        menuToggle.innerHTML = '<i class="fas fa-bars"></i>';
                    }

                    // Прокрутка
                    window.scrollTo({
                        top: targetElement.offsetTop - 100,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });

    // Подсветка активного раздела при скролле
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');

    function highlightNavLink() {
        let scrollPosition = window.scrollY + 150;

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            const sectionId = section.getAttribute('id');

            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${sectionId}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }

    // Инициализация подсветки
    highlightNavLink();
    window.addEventListener('scroll', highlightNavLink);

    // Анимация появления элементов
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

    // Наблюдаем за элементами
    document.querySelectorAll('.category-card, .service-card, .contact-item, .hero, .about-content').forEach(el => {
        observer.observe(el);
    });

    // Обновляем год в подвале
    const yearElements = document.querySelectorAll('.current-year');
    yearElements.forEach(el => {
        el.textContent = new Date().getFullYear();
    });

    console.log('Сайт загружен! Авторские книги ждут своих читателей 📚');
});