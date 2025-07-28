from fastapi import APIRouter
from data.db import scores_db

router = APIRouter()

# ✅ Leaderboard route
@router.get("/leaderboard/")
def get_leaderboard():
    if not scores_db:
        return {"message": "No scores available yet."}

    # Sort scores descending
    sorted_scores = sorted(scores_db.items(), key=lambda x: x[1], reverse=True)
    
    leaderboard = [{"username": username, "score": score} for username, score in sorted_scores]
    
    return {"leaderboard": leaderboard}
