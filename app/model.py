from sqlalchemy import Column, Integer, String, DateTime, Boolean
from config import Base

class Todolist(Base):
    __tablename__ = 'todolist'

    id = Column(Integer, primary_key=True)
    task = Column(String)
    start_date = Column(DateTime)
    due_date = Column(DateTime)
    status = Column(Boolean)