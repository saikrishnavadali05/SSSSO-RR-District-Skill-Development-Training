from pydantic import BaseModel
from typing import List, Optional

class Question(BaseModel):
    id: int
    question: str
    options: List[str]
    correct_answer: str
    category: Optional[str] = None
    difficulty: Optional[str] = None

class Answer(BaseModel):
    question_id: int
    answer: str

class UserLogin(BaseModel):
    username: str
    password: str