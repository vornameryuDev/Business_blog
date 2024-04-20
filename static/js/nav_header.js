const signInBtn = document.querySelector('header div.nav-btn span:first-child');
const logInBtn = document.querySelector('header div.nav-btn span:nth-child(2)');

function signIn() {
    location.href = this.dataset.uri;
}
function logIn() {
    location.href = this.dataset.uri;
}

signInBtn.addEventListener('click', signIn);
logInBtn.addEventListener('click', logIn);