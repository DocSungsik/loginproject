from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base

DB_URL = 'mysql+aiomysql://root:kkss3486!@127.0.0.1:3306/loginproject?charset=utf8'

db_engine = create_async_engine(DB_URL, echo = True)
db_session = async_sessionmaker(autocommit=False, autoflush=False, expire_on_commit=False, bind=db_engine, class_=AsyncSession)

Base = declarative_base()

async def get_db():
    async with db_session() as session:
        yield session