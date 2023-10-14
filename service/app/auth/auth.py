from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

secret_key = "YOUR_SECRET_KEY"
algorithm = "HS256"


def generate_access_token(username: str) -> str:
    token_payload = {"sub": username}
    access_token = jwt.encode(token_payload, secret_key, algorithm)
    return access_token.decode("utf-8")


@router.post("/token")
def get_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {"access_token": generate_access_token(form_data.username), "token_type": "bearer"}


@router.get("/protected")
def protected_route(token: str = Depends(oauth2_scheme)):
    # Your logic for client authentication goes here
    # Example: you can check the token against a database or validate its authenticity

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return {"message": "Access granted"}
