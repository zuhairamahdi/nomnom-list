from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import models.user
import auth, schemas, models
from database import get_db
from sqlalchemy.future import select

import schemas.user

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=schemas.user.UserOut)
async def register(user: schemas.user.UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.user.User).where(models.user.User.email == user.email))
    if result.scalar():
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = models.User(email=user.email, hashed_password=auth.hash_password(user.password))
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

@router.post("/token")
async def login(form_data=Depends(auth.oauth2_scheme), db: AsyncSession = Depends(get_db)):
    # Replace with OAuth2PasswordRequestForm if using username/password form
    return {"access_token": form_data, "token_type": "bearer"}
