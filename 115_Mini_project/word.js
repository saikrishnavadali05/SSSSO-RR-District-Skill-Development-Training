const words = [
    { scrambled: "sgnid", correct: "dings" },
    { scrambled: "rtoal", correct: "toral" },
    { scrambled: "taeos", correct: "soate" },
];

for (let i = 0; i < words.length; i++) {
    const wordElement = document.getElementById(`word-${i + 1}`);
    const inputElement = document.getElementById(`input-${i + 1}`);
    const checkButton = document.getElementById(`check-${i + 1}`);
    const resultElement = document.getElementById(`result-${i + 1}`);

    wordElement.textContent = words[i].scrambled;

    checkButton.addEventListener("click", () => {
        const userInput = inputElement.value.trim().toLowerCase();
        if (userInput === words[i].correct.toLowerCase()) {
            resultElement.textContent = "Correct!";
            resultElement.classList.add("correct");
            resultElement.classList.remove("incorrect");
        } else {
            resultElement.textContent = "Incorrect. Try again!";
            resultElement.classList.add("incorrect");
            resultElement.classList.remove("correct");
        }
    });
}
