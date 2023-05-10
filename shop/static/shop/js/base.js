const navBarActivate = () => {
    document.querySelector('.nav-bar').classList.add('nav-bar-active')
}

const narBarDeactivate = () => {
    document.querySelector('.nav-bar').classList.remove('nav-bar-active')
}

document.querySelector('.nav-btn').addEventListener('click', navBarActivate)
document.querySelector('.close-nav-bar-btn').addEventListener('click', narBarDeactivate)