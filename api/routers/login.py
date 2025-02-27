from fastapi import APIRouter, Depends, HTTPException, Response, Request
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.login as login_schema
import api.cruds.login as login_crud
from api.db import get_db
from jose import jwt, JWTError

from datetime import timedelta

#JWT 인증 토큰
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter()

@router.post("/signup")
async def create_user_test(new_user: login_schema.NewUserCreate, db: AsyncSession = Depends(get_db)):
    #회원 존재 여부 확인
    user = await login_crud.get_user_by_email(new_user.email, db)

    if user:
        raise HTTPException(status_code=409, detail="User already exists")
    
    #회원 가입
    await login_crud.create_user(new_user, db)
    return HTTPException(status_code=200, detail="Signup successful")

@router.post("/login")
async def login(response: Response, login_form: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    #회원 존재 여부 확인
    user = await login_crud.get_user_by_email(login_form.username, db)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid user or password")
    
    res = await login_crud.verify_password(login_form.password, user.hashed_pw)
    if not res:
        raise HTTPException(status_code=400, detail="Invalid user or password")
    
    #토큰 발급
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = await login_crud.create_access_token(data={"sub": login_form.username}, expires_delta=access_token_expires)

    #httpOnly & Secure 쿠키 설정
    response.set_cookie(key="access_token", value=access_token, httponly=True, secure=True, samesite="Lax")

    return {"access_token": access_token, "token_type": "bearer"}

#JWT 검증 API
@router.get("/protected")
async def protected_route(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Unauthorized")

    try:
        payload = jwt.decode(token, login_crud.SECRET_KEY, algorithms=[login_crud.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="invalid token")
        return {"message": f"Hello, {username}"}
    except JWTError:
        raise HTTPException(status_code=401, detail="invalid token")

@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie("access_token")
    return {"message": "logout successful"}

@router.put("/login")
async def change_user_test():
    pass

@router.delete("/login")
async def delete_user_test():
    pass

