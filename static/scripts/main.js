let setting = document.querySelector('.js-click')
let menu = document.querySelector('.menu')
setting.addEventListener("click", () => {
        menu.classList.add('show')
        setTimeout(() => {
                menu.classList.remove('show')
        }, 5000)
})
