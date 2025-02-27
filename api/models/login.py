from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, Mapped, mapped_column
import datetime
from api.db import Base

class User(Base):
    __tablename__ = "users"

    user_no : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id : Mapped[str] = mapped_column(String(10), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    hashed_pw: Mapped[str] = mapped_column(String(100), nullable=False)
    role: Mapped[str] = mapped_column(String(20), nullable=False, default='MEMBER')
    status: Mapped[str] = mapped_column(String(1), nullable=False, default='1')
    regdate: Mapped[datetime.date] = mapped_column(Date, nullable=False, default=datetime.datetime.now)


    