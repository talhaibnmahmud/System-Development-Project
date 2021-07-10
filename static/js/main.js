// user menu
const userMenuBtn = document.querySelector('#user-menu');
const userDropDown = document.querySelector('#user-dropdown');

// mobile menu
const menuToggle = document.querySelector('#menu-toggle');
const mobileMenu = document.querySelector('#mobile-menu');
const hamburger = document.querySelector('#hamburger');
const close = document.querySelector('#close');

userMenuBtn?.addEventListener('click', () => {
    if (userDropDown?.classList.contains('hidden'))
        userDropDown?.classList.replace('hidden', 'block');
    else
        userDropDown?.classList.replace('block', 'hidden');
});

menuToggle?.addEventListener('click', () => {
    if(mobileMenu?.classList.contains('hidden')) {
        close?.classList.replace('hidden', 'block');
        hamburger?.classList.replace('block', 'hidden');
    } else {
        hamburger?.classList.replace('hidden', 'block');
        close?.classList.replace('block', 'hidden');
    }

    mobileMenu?.classList.toggle('hidden');
});
