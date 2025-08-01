from fastapi import APIRouter, HTTPException, Depends
import httpx
import html

from models.schemas import Question, Answer
from data.db import quiz_db, scores_db, users_db, save_scores
from services.auth_service import get_current_user

router = APIRouter()

# ✅ Import questions from Open Trivia API
@router.get("/import-questions/")
async def import_questions(amount: int = 5, category: int = None, difficulty: str = "easy"):
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

    return {"imported": len(new_questions), "questions": new_questions}


# ✅ Get questions (filterable by category & difficulty)
@router.get("/questions/")
def get_questions(category: str = None, difficulty: str = None):
    results = quiz_db
    if category:
        results = [q for q in results if q.category.lower() == category.lower()]
    if difficulty:
        results = [q for q in results if q.difficulty.lower() == difficulty.lower()]
    
    return results


# ✅ Submit an answer and calculate score
@router.post("/answer/")
def submit_answer(answer: Answer, username: str = Depends(get_current_user)):
    for question in quiz_db:
        if question.id == answer.question_id:
            is_correct = question.correct_answer == answer.answer
            scores_db[username] = scores_db.get(username, 0)
            if is_correct:
                scores_db[username] += 1

            save_scores()

            return {
                "your_answer": answer.answer,
                "correct_answer": question.correct_answer,
                "result": "Correct" if is_correct else "Wrong",
                "score": scores_db[username]
            }
    
    raise HTTPException(status_code=404, detail="Question not found")
