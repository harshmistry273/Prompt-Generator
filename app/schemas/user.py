# IMPORTS
from pydantic import BaseModel, EmailStr, Field


# CREATE USER
class CreateUser(BaseModel):
    user_name: str
    email: EmailStr
    password: str


# LOGIN
class LoginUser(BaseModel):
    email: EmailStr
    password: str
    confirm_password: str