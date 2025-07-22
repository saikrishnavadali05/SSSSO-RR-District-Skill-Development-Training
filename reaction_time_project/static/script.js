let waiting = false;
let startTime = 0;
let triggerColor = "green";

// Event listeners
document.getElementById("startBtn").addEventListener("click", startTest);
document.getElementById("theme").addEventListener("change", updateTheme);

// Theme handling
async function updateTheme() {
  const theme = document.getElementById("theme").value;
  const res = await fetch("/theme", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ theme })
  });

  const data = await res.json();
  triggerColor = data.trigger || "green";
  document.body.style.backgroundColor = data.bg;

  if (data.fg) {
    document.querySelectorAll("h1, h3, p, label, #status").forEach(el => {
      el.style.color = data.fg;
    });
  } else {
    document.querySelectorAll("h1, h3, p, label, #status").forEach(el => {
      el.style.color = "";
    });
  }
}

// Start test
function startTest() {
  document.getElementById("status").innerText = "Get Ready...";
  waiting = false;

  setTimeout(() => {
    document.getElementById("status").innerText = "Wait for it...";
    const delay = Math.random() * 3000 + 2000;
    setTimeout(trigger, delay);
  }, 1000);
}

// Trigger color
function trigger() {
  document.getElementById("status").innerText = "PRESS any key NOW!";
  document.body.style.backgroundColor = triggerColor;
  startTime = performance.now();
  waiting = true;
}

// Capture reaction
document.addEventListener("keydown", async () => {
  if (waiting) {
    const reaction = (performance.now() - startTime) / 1000;
    waiting = false;

    let feedback = '';
    if (reaction < 0.2) {
      feedback = '⚡ Super Fast!';
    } else if (reaction < 0.4) {
      feedback = '👌 Good!';
    } else {
      feedback = '🐢 Too slow!';
    }

    document.getElementById("status").innerText = `Your reaction time: ${reaction.toFixed(3)} sec\n${feedback}`;
    document.body.style.backgroundColor = "white";

    const res = await fetch("/record", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ time: reaction })
    });

    const data = await res.json();
    const board = document.getElementById("leaderboard");
    board.innerHTML = "";
    data.scores.forEach((score, i) => {
      const li = document.createElement("li");
      li.innerText = `${i + 1}. ${score.toFixed(3)} sec`;
      board.appendChild(li);
    });
  }
});
