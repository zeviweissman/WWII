from config.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Relationship


class Target(Base):
    __tablename__ = "target"
    id = Column(Integer, primary_key=True, autoincrement=True)
    priority = Column(String)
    location_id = Column(Integer, ForeignKey("location.id"))
    type_id = Column(Integer, ForeignKey("type.id"))
    location = Relationship("Location", back_populates="targets", lazy="joined")
    type = Relationship("Type", back_populates='targets', lazy="joined")

    __table_args__ = (
        UniqueConstraint('priority', 'location_id', 'type_id', name='uq_priority_location_type'),
    )
    def __repr__(self):
        return f"id:{self.id}, priorty:{self.priority}, location:{self.location}, type:{self.type}"