
import json
import random
import time

def load_questions(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return []

def countdown(seconds=5):
    print("\nGet ready! The next question appears in:")
    for i in range(seconds, 0, -1):
        print(f"{i}...", end='', flush=True)
        time.sleep(1)
        print(" ", end='')
    print("\n")

def get_user_answer():
    answer = input("Your answer (1-4): ").strip()
    if answer not in ['1', '2', '3', '4']:
        print("Invalid input. Moving to next question.\n")
        return None
    else:
        return int(answer)

def run_quiz(questions):
    score = 0
    print("\nWelcome to the Quiz!")
    print("Answer each question by typing 1-4 and pressing Enter.\n")

    random.shuffle(questions)  # Shuffle question order

    for i, q in enumerate(questions, start=1):
        countdown(5)  # 5-second countdown before each question
        print(f"Q{i}: {q['question']}")
        options = q['options'][:]
        random.shuffle(options)

        correct_answer_text = q['options'][q['answer'] - 1]
        correct_index = options.index(correct_answer_text) + 1

        for idx, opt in enumerate(options, start=1):
            print(f"  {idx}. {opt}")

        user_choice = get_user_answer()

        if user_choice is None:
            print(f"The correct answer was: {correct_answer_text}\n")
            continue

        if user_choice == correct_index:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was: {correct_answer_text}\n")

    print(f"Quiz finished! You scored {score} out of {len(questions)}.")
    print(f"Your percentage: {(score / len(questions)) * 100:.2f}%")

if __name__ == "__main__":
    filename = "quiz.json"
    questions = load_questions(filename)
    if questions:
        run_quiz(questions)
