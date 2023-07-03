from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session 
import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind = engine)

app = FastAPI()

item = []

class Item(BaseModel):
    item_name : str
    price : int

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally: 
        db.close
    
@app.get("/Item")
def getItem(db:Session = Depends(get_db)):
    return db.query(models.Items).all()

@app.post("/postItem")
def postItem(Hitem:Item, db:Session = Depends(get_db)):
    item_model = models.Items()

    item_model.item_name = Hitem.item_name
    item_model.price = Hitem.price

    db.add(item_model)
    db.commit()

    return ("Wohooo")

@app.put("/EDITHitem/{item_id}")
def EDIThitam(item_id: int, Hitem:Item, db:Session = Depends(get_db)):
    item_model = db.query(models.Items).filter(models.Items.id == item_id).first()

    if item_model.item_name != None:
        item_model.item_name = Hitem.item_name
    if item_model.price != None:
        item_model.price = Hitem.price
    
    db.add(item_model)
    db.commit()
    return ("yayyy")

@app.delete("/hilangkau/{item_id}")
def byebye(item_id:str, db:Session = Depends(get_db)):
    item_model = db.query(models.Items).filter(models.Items.id == item_id).first()

    if item_model is None: 
        return("FUCK YOU")
    
    db.query(models.Items).filter(models.Items.id == item_id).delete()
    db.commit()

    return ("Gone")





