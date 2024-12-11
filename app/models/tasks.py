from backend.db import Base
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from models import *

class Tasks(Base):
    __tablename__="Tasks"
    __table_args__= {'extend_existing': True}
    id= Column(Integer, primary_key=True, index=True)
    title =  Column(String)
    content = Column(String)
    priority = Column(Integer, default = 0)

    slug = Column(String, unique= True, index=True)
    completed = Column(Boolean, default=False)
    user_id  = Column(Integer, ForeignKey("User.id"), nullable=True, index= True)

    user = relationship('User',back_populates='tasks')


from sqlalchemy.schema import CreateTable
print(CreateTable(Tasks.__table__))