import os
import json
from fastapi import HTTPException
from passlib.context import CryptContext
from models.schemas import UserLogin
from data.db import users_db, save_users

# ✅ Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ✅ Hash plain password
def hash_password(password: str):
    return pwd_context.hash(password)

# ✅ Verify password
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

# ✅ Register new user
def register_user(user: UserLogin):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_pwd = hash_password(user.password)
    users_db[user.username] = {
        "username": user.username,
        "password": hashed_pwd
    }

    save_users()
    return {"message": "User registered successfully"}

# ✅ Login existing user
def login_user(user: UserLogin):
    db_user = users_db.get(user.username)
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {"message": "Login successful", "username": user.username}

# ✅ For use with Depends in protected routes
def get_current_user(username: str):
    if username not in users_db:
        raise HTTPException(status_code=401, detail="Invalid user")
    return username
