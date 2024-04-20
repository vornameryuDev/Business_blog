const logoBtn = document.querySelector('.nav-title');
const signInBtn = document.querySelector('header div.nav-btn span:first-child');
const logInBtn = document.querySelector('header div.nav-btn span:nth-child(2)');

function logo() {
    location.href = this.dataset.uri;
}
function signIn() {
    location.href = this.dataset.uri;
}
function logIn() {
    location.href = this.dataset.uri;
}

logoBtn.addEventListener('click', logo);
signInBtn.addEventListener('click', signIn);
logInBtn.addEventListener('click', logIn);