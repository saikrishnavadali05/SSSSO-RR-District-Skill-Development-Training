from fastapi import FastAPI, HTTPException
from schemas import UserRegister, UserLogin, QuizAnswer
from passlib.context import CryptContext
from data import get_users, save_users, get_scores, save_scores
import httpx
import random

app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ---- Register ----
@app.post("/register")
def register(user: UserRegister):
    users = get_users()
    if user.username in users:
        raise HTTPException(status_code=400, detail="User already exists")
    hashed = pwd_context.hash(user.password)
    users[user.username] = {"password": hashed}
    save_users(users)
    return {"msg": "Registered successfully"}

# ---- Login ----
@app.post("/login")
def login(user: UserLogin):
    users = get_users()
    db_user = users.get(user.username)
    if not db_user or not pwd_context.verify(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"msg": "Login successful"}

# ---- Import Quiz Questions ----
@app.get("/quiz/")
async def get_quiz(category: int = 9, difficulty: str = "easy", limit: int = 5):
    url = f"https://opentdb.com/api.php?amount={limit}&category={category}&difficulty={difficulty}&type=multiple"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
    return data["results"]

# ---- Submit Answer ----
@app.post("/submit/")
def submit_answer(answer: QuizAnswer):
    scores = get_scores()
    if answer.username not in scores:
        scores[answer.username] = {"score": 0, "answers": []}

    correct_answer = answer.question.split("::")[-1]  # Sample way to store and validate
    is_correct = answer.answer.strip().lower() == correct_answer.strip().lower()
    if is_correct:
        scores[answer.username]["score"] += 1

    scores[answer.username]["answers"].append({
        "question": answer.question,
        "user_answer": answer.answer,
        "correct": correct_answer,
        "result": "correct" if is_correct else "wrong"
    })

    save_scores(scores)
    return {"result": "correct" if is_correct else "wrong"}

# ---- Leaderboard ----
@app.get("/leaderboard")
def leaderboard():
    scores = get_scores()
    leaderboard = sorted(scores.items(), key=lambda x: x[1]["score"], reverse=True)
    return [{"username": k, "score": v["score"]} for k, v in leaderboard]
