from config.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Relationship


class Country(Base):
    __tablename__ = "country"
    id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String, nullable=False)
    locations = Relationship("Location", back_populates='country')


    def __repr__(self):
        return f"id:{self.id}, country:{self.country}"