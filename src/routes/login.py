from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from src.service.user_service import UserService

from src.db.session import get_db
from src.schemas.user_schemas import(
    UserSignup,
    UserLogin,
    UserResponse
)

router = APIRouter(
    prefix="/auth",
    tags=["user"]
)

@router.post("/singup")
def singin(
    user_data : UserSignup,
    db : Session = Depends(get_db)
):
    service = UserService(db)

    try:
        return service.register_user(
            user_data
        )
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        )

