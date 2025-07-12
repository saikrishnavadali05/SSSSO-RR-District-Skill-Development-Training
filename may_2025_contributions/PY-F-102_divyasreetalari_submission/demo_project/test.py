import requests
import html
import random

def fetch_questions(amount=5):
    url = f"https://opentdb.com/api.php?amount={amount}&type=multiple"
    response = requests.get(url)
    data = response.json()
    l = list(response)
    for i in range(10):
        print(l[i])
    return data['results']
#print(response)
fetch_questions()
"""
def start_quiz():
    score = 0
    questions = fetch_questions()
    
    for index, q in enumerate(questions):
        print(f"\nQ{index + 1}: {html.unescape(q['question'])}")
        options = q['incorrect_answers'] + [q['correct_answer']]
        random.shuffle(options)

        for i, option in enumerate(options):
            print(f"{i + 1}. {html.unescape(option)}")

        answer = input("Your answer (1-4): ")
        try:
            if html.unescape(options[int(answer) - 1]) == html.unescape(q['correct_answer']):
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {html.unescape(q['correct_answer'])}")
        except:
            print("⚠️ Invalid input, skipping question.")

    print(f"\n🎯 Final Score: {score} / {len(questions)}")

if __name__ == "__main__":
    start_quiz()"""