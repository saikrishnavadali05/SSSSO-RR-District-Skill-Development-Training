import random
from collections import deque
from django.shortcuts import render
import os

categories = {
    "Yes, definitely": "positive",
    "Without a doubt": "positive",
    "You may rely on it": "positive",
    "Reply hazy, try again": "neutral",
    "Ask again later": "neutral",
    "Don’t count on it": "negative",
    "My reply is no": "negative",
    "Very doubtful": "negative"
}

history = deque(maxlen=5)
questions = []

def home(request):
    return render(request, "game/welcome.html")

def play(request):
    response_data = None
    

    if request.method == "POST":
        question = request.POST.get("question")

        if question and question.lower() != "exit":
            questions.append(question)
            answer = random.choice(list(categories.keys()))
            history.append((question, answer))
            response_data = {"question": question, "answer": answer, "type": categories[answer]}

            with open("response.txt", "a", encoding="utf-8") as f:
                f.write(f"Question: {question}\n")
                f.write(f"Response: {str(response_data)}\n\n")

    # all_history = [q.split("Question: ")[-1].strip() for q in open("response.txt", encoding="utf-8").read().split("Question: ") if q.strip() and "Response:" in q]
    all_history = [q.split("Question: ")[-1].strip() for q in open("response.txt", encoding="utf-8").read().split("Question: ") if q.strip() and "Response:" in q]

    return render(request, "game/game.html", {
        "response": response_data,
        "history": list(history),
        "all_history": all_history
    })
