from config.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Relationship


class Type(Base):
    __tablename__ = "type"
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String, nullable=False)
    targets = Relationship("Target", back_populates='type')


    def __repr__(self):
        return f"id:{self.id}, type:{self.type}"