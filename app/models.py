from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from app.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    is_active = Column(Boolean, default=True)
