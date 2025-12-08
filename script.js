// Основной скрипт для сайта
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

    // Мобильное выпадающее меню
    const dropdownToggles = document.querySelectorAll('.dropdown-toggle');

    dropdownToggles.forEach(toggle => {
        toggle.addEventListener('click', function(e) {
            if (window.innerWidth <= 768) {
                e.preventDefault();
                const dropdown = this.parentElement;
                dropdown.classList.toggle('active');
            }
        });
    });

    // Плавная прокрутка
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');

            if (href !== '#' && href.startsWith('#')) {
                e.preventDefault();
                const targetElement = document.querySelector(href);

                if (targetElement) {
                    // Закрываем мобильное меню если открыто
                    if (window.innerWidth <= 768 && mainNav) {
                        mainNav.classList.remove('active');
                        menuToggle.innerHTML = '<i class="fas fa-bars"></i>';
                    }

                    // Добавляем анимацию к целевой секции
                    targetElement.classList.add('animated');

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
    const navLinks = document.querySelectorAll('.nav-link, .dropdown-item');

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

    // Анимация книг
    const books = document.querySelectorAll('.book');
    if (books.length > 0) {
        setTimeout(() => {
            books.forEach((book, index) => {
                setTimeout(() => {
                    book.style.transition = 'transform 0.5s ease';
                    book.style.transform = book.style.transform.replace(/translateZ\([^)]*\)/, 'translateZ(20px)');

                    setTimeout(() => {
                        book.style.transform = book.style.transform.replace(/translateZ\([^)]*\)/, 'translateZ(10px)');
                    }, 300);
                }, index * 200);
            });
        }, 1000);
    }

    console.log('Сайт загружен! Авторские книги ждут своих читателей 📚');
});