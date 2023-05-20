const forward = () => {
    window.location.replace("/home")
}

const changeMainText = (text) => {
    const mainText = document.getElementById("mainText")
    mainText.innerText = text
}

text = [
    "БЕЗПЕЧНИЙ ЗВ'ЯЗОК ТУТ",
    "ТИ ОБИРАЄШ СВОБОДУ?",
    "ДОЛУЧАЙСЯ ДО НАШОЇ СПІЛЬНОТИ",
    "РАБІВ У МАТРИЦЮ НЕ ПУСКАЮТЬ"
]

text.sort(() => Math.random() - 0.5);

text.map(
    (text, index) => {
        setTimeout(() => {
            changeMainText(text)
        }, (index + 1) * 3000)
    }
)