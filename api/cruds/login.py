from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result

import api.models.login as login_model
import api.schemas.login as login_schema

from passlib.context import CryptContext
from datetime import timedelta, datetime
from jose import JWTError, jwt

#시크릿 키 및 알고리즘 설정
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"


#비밀번호 해싱 설정
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_user_by_email(email: str, db: AsyncSession) -> login_model.User | None:
    result: Result = await db.execute(
        select(login_model.User).filter(login_model.User.email == email)
    )
    return result.scalars().first()

async def create_user(new_user: login_schema.NewUserCreate, db: AsyncSession) -> login_model.User:
    user = login_model.User(user_id = new_user.id, 
                            email = new_user.email, 
                            hashed_pw = pwd_context.hash(new_user.password))
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

#JWT 생성 함수
async def create_access_token(data:dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.now() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)