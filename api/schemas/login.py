from pydantic import BaseModel, Field, EmailStr, field_validator
from fastapi import HTTPException

class UserBase(BaseModel):
    id: str
    password: str

class NewUserCreate(UserBase):
    email: EmailStr
    phone: str

    @field_validator('id', 'password', 'phone', 'email')
    @classmethod
    def check_empty(cls, v):
        if not v or v.isspace():
            raise HTTPException(status_code=422, detail="필수 항목을 입력시켜주세요.")
        return v
    
    @field_validator('phone')
    @classmethod
    def check_phone(cls, v):
        phone = v
        if '-' not in v or len(phone)!=13:
            raise HTTPException(status_code=422, detail="핸드폰 번호를 000-0000-0000 형식으로 입력해 주세요.")
        return v
    
    @field_validator('password')
    @classmethod
    def validate_password(cls, v):
        if len(v) < 8:
            raise HTTPException(status_code=422, detail="비밀번호는 8자리 이상 영문과 숫자를 포함하여 작성해주세요.")
        if not any(char.isdigit() for char in v):
            raise HTTPException(status_code=422, detail="비밀번호는 8자리 이상 영문과 숫자를 포함하여 작성해주세요.")
        if not any(char.isalpha() for char in v):
            raise HTTPException(status_code=422, detail="비밀번호는 8자리 이상 영문과 숫자를 포함하여 작성해주세요.")
        
        return v
