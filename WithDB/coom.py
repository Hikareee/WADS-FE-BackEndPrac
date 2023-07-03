from fastapi import FastAPI, Depends
import models
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from fastapi.exceptions import HTTPException
app = FastAPI()

cum= []

true = True
false = False
    
models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class kum(BaseModel):
    seed_name : str
    makePregant : bool

@app.get("/cum")
def getCum(db:Session = Depends(get_db)):
    return db.query(models.cuming).all()

@app.get("coom/{seed_name}")
def getbyName(seed_nam:str ,db: Session = Depends(get_db)):
    if models.cuming.seed_name in models.cuming:
        return db.query(models.cuming).filter(models.cuming.seed_name == seed_nam).first()
    else: 
        return("Fuck you")

@app.post("/postCum")
def postCum(payload:kum, db: Session = Depends(get_db)):
    if models.cuming.seed_id in cum:
        return{"Error": "Your seed exists"}
    
    cum_model = models.cuming()
    cum_model.seed_name = payload.seed_name
    cum_model.makePregant = payload.makePregant

    db.add(cum_model)
    db.commit()

    return payload

@app.put("/editCum/{seed_id}")
def editCum(seed_id:int, Kum:kum, db:Session = Depends(get_db)):
    cum_model = db.query(models.cuming).filter(models.cuming.seed_id == seed_id).first()
    
    if cum_model is None:
        return("Fuck You Nigga")
    if cum_model.seed_name != None: 
        cum_model.seed_name = Kum.seed_name
    if cum_model.makePregant != None:
        cum_model.makePregant = Kum.makePregant
    
    db.add(cum_model)
    db.commit()
    return Kum

@app.delete("/{seed_id}")
def deleteSeed(seed_id:int, db:Session = Depends(get_db)):
    cum_model = db.query(models.cuming).filter(models.cuming.seed_id == seed_id).first()

    if cum_model is None:
        return ("Fuck Off")
    
    db.query(models.cuming).filter(models.cuming.seed_id == seed_id).delete
    db.commit 

    return ("Abortion Bitch")
