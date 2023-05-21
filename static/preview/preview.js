const forward = () => {
    window.location.replace("/home")
}

const changeMainText = (text) => {
    const mainText = document.getElementById("mainText")
    mainText.innerText = text
}


const setTextList = (external_text) => {
    let text = [
        "БЕЗПЕЧНИЙ ЗВ'ЯЗОК ТУТ",
        "ТИ ОБИРАЄШ СВОБОДУ?",
        "ДОЛУЧАЙСЯ ДО НАШОЇ СПІЛЬНОТИ",
        "РАБІВ У МАТРИЦЮ НЕ ПУСКАЮТЬ"
    ]

    if (external_text != null) {
        phrases = JSON.parse(external_text).phrases
        if (phrases.length > 0) {
            text = phrases
        }
    }

    text.map(
        (text, index) => {
            setTimeout(() => {
                changeMainText(text)
            }, (index + 1) * 5000)
        }
    )
}