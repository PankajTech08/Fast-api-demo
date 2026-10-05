from fastapi import APIRouter

from src.models.user import User

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/{user_id}", response_model=User)
def read_user(user_id: int) -> User:
    return User(id=user_id, name="Example User", email="user@example.com")
