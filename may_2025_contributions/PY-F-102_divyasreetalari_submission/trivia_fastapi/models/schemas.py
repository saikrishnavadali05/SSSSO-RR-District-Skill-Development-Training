from pydantic import BaseModel, ConfigDict
from typing import List


# ✅ Model for user registration/login
class UserLogin(BaseModel):
    username: str
    password: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "username": "john_doe",
                "password": "secret123"
            }
        }
    )


# ✅ Optional public user model (without password)
class UserPublic(BaseModel):
    username: str


# ✅ Model for quiz question
class Question(BaseModel):
    id: int
    question: str
    options: List[str]
    correct_answer: str
    category: str
    difficulty: str


# ✅ Model for answer submission
class Answer(BaseModel):
    question_id: int
    answer: str
