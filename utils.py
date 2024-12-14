from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "2ba3594354d4eb2251b0312ed878273f67d8760acdd9319731ccc4647ae623e2"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing context
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Helper functions for password hashing
def get_hashed_password(password: str):
    return password_context.hash(password)

def verify_password(password: str, hashed_password: str):
    return password_context.verify(password, hashed_password)

# JWT token creation
def create_access_token(subject: str, expires_delta: timedelta = None) -> str:
    if expires_delta:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # jwt package contains sub for username, exp is expiry time
    to_encode = {"exp": expires_delta, "sub": subject}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt