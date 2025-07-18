async function checkPalindrome() {
  const text = document.getElementById("inputText").value;

  try {
    const response = await fetch("/check", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text: text }),
    });

    const data = await response.json();
    document.getElementById("result").innerText = data.result;
  } catch (error) {
    console.error("Error:", error);
  }
}
