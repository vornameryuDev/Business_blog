const logoBtn = document.querySelector('.nav-title');

function logo() {
    location.href = this.dataset.uri;
}

logoBtn.addEventListener('click', logo);
