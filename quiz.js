// quiz.js
let currentQuestion = 0;
let score = 0;
let questions = [];

fetch("questions.json")
  .then((res) => res.json())
  .then((data) => {
    questions = data;
    showQuestion();
  });

function showQuestion() {
  const q = questions[currentQuestion];
  document.getElementById("question").innerText = q.question;
  const options = document.getElementById("options");
  options.innerHTML = "";
  q.options.forEach((opt, index) => {
    const li = document.createElement("li");
    li.innerHTML = `<input type='radio' name='option' value='${index}' /> ${opt}`;
    options.appendChild(li);
  });
}

document.getElementById("next-btn").addEventListener("click", () => {
  const selected = document.querySelector("input[name='option']:checked");
  if (!selected) return alert("Please select an option");
  if (parseInt(selected.value) === questions[currentQuestion].answer) score++;
  currentQuestion++;
  if (currentQuestion < questions.length) {
    showQuestion();
  } else {
    document.getElementById("quiz-container").style.display = "none";
    document.getElementById("score-box").style.display = "block";
    document.getElementById("score").innerText = `${score}/${questions.length}`;
  }
});
