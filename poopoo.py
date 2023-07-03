from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import UUID
from typing import Optional

app = FastAPI()

class poopoo(BaseModel):
    name : str
    iz : str
    G : str

class updatepoopoo(BaseModel):
    name: Optional[str] = None
    iz: Optional[str] = None
    G: Optional[str] = None

POOS = []

@app.get("/getBagz")
def getBagz():
    return(POOS)

@app.post("/postBagz")
def postBagz(Poopoo:poopoo):
    POOS.append(Poopoo)
    return Poopoo

@app.put("/editBagz/{bagz_id}")
def editBagz(bagz_id: int, Poopoo:updatepoopoo):
    if bagz_id not in POOS:
        return{"Error": "Iz no exist"}
    if Poopoo.name != None:
        POOS[bagz_id].name = Poopoo.name
    if Poopoo.iz != None:
        POOS[bagz_id].iz = Poopoo.iz
    if Poopoo.G != None:
        POOS[bagz_id].G = Poopoo.G

@app.delete("/byebyenigga/{bagz_id}")
def del_bagz(bagz_id: int):
    if bagz_id not in POOS:
        return {"Fuck you":"No id bitch"}
    del POOS[bagz_id]
    return{"Fuck baguz"}
