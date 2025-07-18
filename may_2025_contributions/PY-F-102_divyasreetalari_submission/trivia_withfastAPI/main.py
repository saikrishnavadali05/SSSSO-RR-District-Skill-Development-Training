from fastapi import FastAPI, HTTPException, Depends
from schemas import Question, Answer, UserLogin
from database import quiz_db, users_db, scores_db
import html
import httpx
import json
import os
from passlib.context import CryptContext
from enum import Enum


app = FastAPI()

class Difficulty(str, Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"

# Password hasher
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Load users from file (if not empty)
if os.path.exists("users.json"):
    try:
        with open("users.json", "r") as f:
            content = f.read().strip()
            if content:
                users_db.update(json.loads(content))
    except Exception as e:
        print("⚠️ Could not load users.json:", e)

# Save users to file
def save_users_to_file():
    with open("users.json", "w") as f:
        json.dump(users_db, f, indent=4)

# Save scores to file
def save_scores_to_file():
    with open("scores.json", "w") as f:
        json.dump(scores_db, f, indent=4)

# Password hashing utilities
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# User authentication (dummy)
def get_current_user(username: str):
    if username not in users_db:
        raise HTTPException(status_code=401, detail="Invalid user")
    return username

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Trivia Quiz! 🎉 Visit /docs to try it out."}

# ------------------ User Routes ------------------

@app.post("/register/")
def register(user: UserLogin):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_pwd = hash_password(user.password)
    users_db[user.username] = {
        "username": user.username,
        "password": hashed_pwd
    }

    save_users_to_file()
    return {"message": "User registered successfully ✅"}

@app.post("/login/")
def login(user: UserLogin):
    db_user = users_db.get(user.username)
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    return {"message": "Login successful 🎉", "username": user.username}

# ------------------ Quiz Routes ------------------

#@app.get("/import-questions/")
#async def import_questions(amount: int = 10, category: int = None, difficulty: str = "easy"):
@app.get("/import-questions/")
async def import_questions(
    amount: int = 10,
    category: int = None,
    difficulty: Difficulty = Difficulty.easy):
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

@app.get("/questions/")
def get_questions(category: str = None, difficulty: str = None):
    results = quiz_db
    if category:
        results = [q for q in results if q.category.lower() == category.lower()]
    if difficulty:
        results = [q for q in results if q.difficulty.lower() == difficulty.lower()]
    return results

@app.post("/answer/")
def submit_answer(answer: Answer, username: str = Depends(get_current_user)):
    for question in quiz_db:
        if question.id == answer.question_id:
            is_correct = question.correct_answer == answer.answer
            scores_db[username] = scores_db.get(username, 0)
            if is_correct:
                scores_db[username] += 1
            save_scores_to_file()

            return {
                "your_answer": answer.answer,
                "correct_answer": question.correct_answer,
                "result": "Correct" if is_correct else "Wrong",
                "score": scores_db[username]
            }
    raise HTTPException(status_code=404, detail="Question not found")

@app.get("/leaderboard/")
def get_leaderboard():
    if not scores_db:
        return {"message": "No scores available yet."}

    sorted_scores = sorted(scores_db.items(), key=lambda x: x[1], reverse=True)
    leaderboard = [{"username": user, "score": score} for user, score in sorted_scores]
    return leaderboard
@app.get("/categories/")
def get_categories():
    return {
        "categories": {
            9: "General Knowledge",
            10: "Books",
            11: "Film",
            12: "Music",
            17: "Science & Nature",
            18: "Computers",
            19: "Mathematics",
            23: "History",
            27: "Animals"
        }
    }
from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="."), name="static")
