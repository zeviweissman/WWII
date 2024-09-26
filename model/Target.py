from config.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Relationship


class Target(Base):
    __tablename__ = "target"
    id = Column(Integer, primary_key=True, autoincrement=True)
    priorty = Column(Integer, nullable=False)
    location_id = Column(Integer, ForeignKey("location.id"))
    type_id = Column(Integer, ForeignKey("type.id"))
    location = Relationship("Location", back_populates="target")
    type = Relationship("Type", back_populates='target')


    def __repr__(self):
        return f"id:{self.id}, priorty:{self.priorty}"