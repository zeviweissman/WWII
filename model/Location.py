from config.base import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import Relationship


class Location(Base):
    __tablename__ = "location"
    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String, nullable=False)
    country_id = Column(Integer, ForeignKey('country.id'))
    lat = Column(Float)
    lon = Column(Float)
    country = Relationship("Country", back_populates='cities', lazy="joined")


    def __repr__(self):
        return f"id:{self.id}, city:{self.city}, lat/lon={self.lat, self.lon}, country:{self.country}"