from sqlalchemy.orm import Session

import models
import schemas


def create_point(db: Session, point: schemas.PointCreate):
    db_point = models.Point(
        name=point.name,
        description=point.description,
        lat=point.lat,
        lng=point.lng,
        category=point.category
    )
    db.add(db_point)
    db.commit()
    db.refresh(db_point)
    return db_point


def get_point(db: Session, point_id: int):
    return db.query(models.Point).filter(models.Point.id == point_id).first()


def get_point_by_lat_lng(db: Session, lat: float, lng: float):
    return db.query(models.Point)\
        .filter(models.Point.lat == lat)\
        .filter(models.Point.lng == lng)\
        .first()


def delete_point(db: Session, point_id):
    point_to_remove = get_point(db, point_id)
    db.delete(point_to_remove)
    db.commit()
    return {'ok': True}


def get_points(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Point).offset(skip).limit(limit).all()


def create_place(db: Session, place: schemas.PlaceCreate):
    db_place = models.Place(
        name=place.name,
        description=place.description,
        lat=place.lat,
        lng=place.lng,
        country=place.country,
        city=place.city,
        postcode=place.postcode,
        street=place.street,
        number=place.number,
        toaletaAkt=place.toaletaAkt,
        toaletaElektr=place.toaletaElektr,
        parking=place.parking,
        winda=place.winda,
        brakProgow=place.brakProgow,
        swobodnyAkt=place.swobodnyAkt,
        swobodnyElektr=place.swobodnyElektr,
        drzwiAkt=place.drzwiAkt,
        drzwiElektr=place.drzwiElektr,
        rownyTeren=place.rownyTeren
    )
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return db_place


def get_place(db: Session, place_id: int):
    return db.query(models.Place).filter(models.Place.id == place_id).first()


def get_place_by_lat_lng(db: Session, lat: float, lng: float):
    return db.query(models.Place)\
        .filter(models.Place.lat == lat)\
        .filter(models.Place.lng == lng)\
        .first()


def delete_place(db: Session, place_id: int):
    place_to_remove = get_place(db, place_id)
    db.delete(place_to_remove)
    db.commit()
    return {'ok': True}


def get_places(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Place).offset(skip).limit(limit).all()
