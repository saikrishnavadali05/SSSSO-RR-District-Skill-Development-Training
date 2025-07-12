import httpx
import html
from fastapi import HTTPException
from models.schemas import Question
from data.db import quiz_db

# ✅ Import questions from Open Trivia DB
async def import_questions_from_api(amount: int = 10, category: int = None, difficulty: str = "easy"):
    url = f"https://opentdb.com/api.php?amount={amount}&difficulty={difficulty}&type=multiple"
    if category:
        url += f"&category={category}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()

    if data["response_code"] != 0:
        raise HTTPException(status_code=500, detail="Failed to fetch trivia questions")

    new_questions = []
    for item in data["results"]:
        options = item["incorrect_answers"] + [item["correct_answer"]]
        shuffled = sorted([html.unescape(opt) for opt in options])

        question_data = Question(
            id=len(quiz_db) + 1,
            question=html.unescape(item["question"]),
            options=shuffled,
            correct_answer=html.unescape(item["correct_answer"]),
            category=item["category"],
            difficulty=item["difficulty"]
        )
        quiz_db.append(question_data)
        new_questions.append(question_data)

    return new_questions

# ✅ Get questions with optional filters
def get_filtered_questions(category: str = None, difficulty: str = None):
    results = quiz_db
    if category:
        results = [q for q in results if q.category.lower() == category.lower()]
    if difficulty:
        results = [q for q in results if q.difficulty.lower() == difficulty.lower()]
    return results

# ✅ Get a question by ID (optional use)
def get_question_by_id(qid: int):
    for q in quiz_db:
        if q.id == qid:
            return q
    raise HTTPException(status_code=404, detail="Question not found")
