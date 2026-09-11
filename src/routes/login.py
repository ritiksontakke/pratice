from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from src.service.user_service import UserService
from src.service.login_service import AuthService
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


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    service = AuthService(db)

    user_data = UserLogin(
        email=form_data.username,
        password=form_data.password,
    )

    try:
        return service.login_user(user_data)

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(error),
            headers={
                "WWW-Authenticate": "Bearer",
            },
        )