from typing import Optional

from pydantic import BaseModel


class PointBase(BaseModel):
    name: Optional[str]
    description: Optional[str] = None
    lat: float
    lng: float
    category: Optional[str] = None


class PointCreate(PointBase):
    pass


class Point(PointBase):
    id: int

    class Config:
        orm_mode = True


class PlaceBase(BaseModel):
    name: Optional[str]
    description: Optional[str] = None
    lat: float
    lng: float
    country: Optional[str]
    city: Optional[str]
    postcode: Optional[str]
    street: Optional[str]
    number: Optional[str]
    toaletaAkt: bool
    toaletaElektr: bool
    parking: bool
    winda: bool
    brakProgow: bool
    swobodnyAkt: bool
    swobodnyElektr: bool
    drzwiAkt: bool
    drzwiElektr: bool
    rownyTeren: bool


class PlaceCreate(PlaceBase):
    pass


class Place(PlaceBase):
    id: int

    class Config:
        orm_mode = True
