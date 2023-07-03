from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from database import Base

class Items(Base):
    __tablename__ = "Items"

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String)
    price = Column(Integer)