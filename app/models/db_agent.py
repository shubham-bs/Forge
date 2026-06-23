from sqlalchemy import Column, Integer, String

from app.core.database import Base


class DBAgent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)