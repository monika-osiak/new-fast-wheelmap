from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal, engine, get_db

import crud
import models
import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/points/", response_model=schemas.Point)
def create_point(point: schemas.PointCreate, db: Session = Depends(get_db)):
    db_point = crud.get_point_by_lat_lng(db, point.lat, point.lng)
    if db_point:
        raise HTTPException(status_code=400, detail="This point already exists")
    return crud.create_point(db=db, point=point)


@app.get("/points/", response_model=list[schemas.Point])
def read_points(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    points = crud.get_points(db, skip=skip, limit=limit)
    return points


@app.get("/points/{point_id}", response_model=schemas.Point)
def read_point(point_id: int, db: Session = Depends(get_db)):
    db_point = crud.get_point(db, point_id=point_id)
    if db_point is None:
        raise HTTPException(status_code=404, detail="Point not found")
    return db_point


@app.post("/places/", response_model=schemas.Place)
def create_place(place: schemas.PlaceCreate, db: Session = Depends(get_db)):
    db_place = crud.get_place_by_lat_lng(db, place.lat, place.lng)
    if db_place:
        raise HTTPException(status_code=400, detail="This place already exists")
    return crud.create_place(db=db, place=place)


@app.get("/places/", response_model=list[schemas.Place])
def read_places(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    places = crud.get_places(db, skip=skip, limit=limit)
    return places


@app.get("/places/{place_id}", response_model=schemas.Place)
def read_place(place_id: int, db: Session = Depends(get_db)):
    db_place = crud.get_place(db, place_id=place_id)
    if db_place is None:
        raise HTTPException(status_code=404, detail="Place not found")
    return db_place