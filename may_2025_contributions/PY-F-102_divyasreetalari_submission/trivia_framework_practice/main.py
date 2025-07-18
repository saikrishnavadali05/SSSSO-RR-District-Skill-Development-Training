from fastapi import FastAPI
from routers import auth, quiz, score

app = FastAPI(title="Trivia Quiz API")

# ✅ Include all routers
app.include_router(auth.router)
app.include_router(quiz.router)
app.include_router(score.router)

# ✅ Welcome route
@app.get("/")
def read_root():
    return {
        "message": "🎉 Welcome to the FastAPI Trivia Quiz!",
        "docs": "Visit /docs to try the API"
    }
