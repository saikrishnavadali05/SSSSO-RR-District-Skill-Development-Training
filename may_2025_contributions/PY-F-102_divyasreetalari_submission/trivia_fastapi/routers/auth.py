from fastapi import APIRouter, HTTPException
from mini_triviaapi_fastapi.models.schemas import UserLogin
from services.auth_service import register_user, login_user

router = APIRouter()

# ✅ Register route
@router.post("/register/")
def register(user: UserLogin):
    return register_user(user)

# ✅ Login route
@router.post("/login/")
def login(user: UserLogin):
    return login_user(user)
