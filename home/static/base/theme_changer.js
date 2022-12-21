const body = document.body

const theme_changer = (number) => {
    if (number===1) {
        body.className = 'old_theme'
        localStorage.setItem('theme_number', '1')
    }
    if (number===2) {
        body.className = 'dark_theme'
        localStorage.setItem('theme_number', '2')
    }
    if (number===3) {
        body.className = 'light_theme'
        localStorage.setItem('theme_number', '3')
    }
}

const set_color_scheme = () => {
    const theme = localStorage.getItem('theme_number')

    if (theme !== undefined) {
        theme_changer(parseInt(theme))
    } else {
        if (window.matchMedia) {
            if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
                // Set dark
                theme_changer(2)
            } else {
                // Set light
                theme_changer(3)
            }
        }
    }
}

set_color_scheme()