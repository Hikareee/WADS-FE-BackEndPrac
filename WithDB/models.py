from database import Base
from sqlalchemy import Integer,String,Column,ForeignKey,Boolean

class cuming(Base):
    __tablename__ = "cum"

    seed_id = Column(Integer, primary_key=True,index = True)
    seed_name = Column(String)
    makePregant = Column(Boolean)

