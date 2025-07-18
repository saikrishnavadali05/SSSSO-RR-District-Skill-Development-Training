from pydantic import BaseModel
from typing import List

class UserRegister(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class Question(BaseModel):
    question: str
    correct_answer: str
    incorrect_answers: List[str]

class QuizAnswer(BaseModel):
    username: str
    question: str
    answer: str
