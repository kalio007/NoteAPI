from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
import os
load_dotenv()

engine = create_engine(
    url= os.getenv('DATABASE_URL'),
    echo=True,
)
class Base(DeclarativeBase):
    pass