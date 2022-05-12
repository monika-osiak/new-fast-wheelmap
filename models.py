from sqlalchemy import Column, Integer, PickleType, String, Boolean, Float

from database import Base


class Point(Base):
    __tablename__ = "points"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    lat = Column(Float, index=True)
    lng = Column(Float, index=True)
    category = Column(String)



class Place(Base):
    __tablename__ = "places"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    lat = Column(Float, index=True)
    lng = Column(Float, index=True)
    country = Column(String)
    city = Column(String)
    postcode = Column(String)
    street = Column(String)
    number = Column(String)
    toaletaAkt = Column(Boolean)
    toaletaElektr = Column(Boolean)
    parking = Column(Boolean)
    winda = Column(Boolean)
    brakProgow = Column(Boolean)
    swobodnyAkt = Column(Boolean)
    swobodnyElektr = Column(Boolean)
    drzwiAkt = Column(Boolean)
    drzwiElektr = Column(Boolean)
    rownyTeren = Column(Boolean)
