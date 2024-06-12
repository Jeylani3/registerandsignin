# File: app/auth.py

from fastapi import APIRouter, HTTPException,  Depends
from pydantic import BaseModel
from passlib.context import CryptContext
from config import get_db_connection


# Define a Pydantic model for user registration input
class UserRegistration(BaseModel):
    username: str
    password: str

# Define a Pydantic model for user login input
class UserLogin(BaseModel):
    username: str
    password: str
    
class LoginRequest(BaseModel):
    username: str
    password: str    

# Create an instance of CryptContext for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Create a router for the authentication endpoints
router = APIRouter()


# Endpoint for user registration
@router.post("/register")
async def register_user(user: UserRegistration):
    # Hash the user's password
    hashed_password = pwd_context.hash(user.password)

    # Store user information in the database
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (user.username, hashed_password)
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to register user: {str(e)}")
    finally:
        cursor.close()
        conn.close()

    return {"message": "User registered successfully"}

# Endpoint for user login
@router.post("/login")
async def login_user(user: UserLogin):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT password FROM users WHERE username = %s", (user.username,))
        result = cursor.fetchone()

        if not result or not pwd_context.verify(user.password, result[0]):
            raise HTTPException(status_code=400, detail="Invalid username or password")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Login failed: {str(e)}")
    finally:
        cursor.close()
        conn.close()

    return {"message": "Login successful"}
