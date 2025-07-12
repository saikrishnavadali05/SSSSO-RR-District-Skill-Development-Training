# Logic to fetch questions

import requests
import html

def get_questions(amount=10):
    url = f"https://opentdb.com/api.php?amount={amount}&type=multiple"
    response = requests.get(url)
    data = response.json()
    questions = []

    for q in data['results']:
        question = {
            "question": html.unescape(q['question']),
            "correct": html.unescape(q['correct_answer']),
            "options": [html.unescape(opt) for opt in q['incorrect_answers'] + [q['correct_answer']]]
        }
        questions.append(question)

    return questions
