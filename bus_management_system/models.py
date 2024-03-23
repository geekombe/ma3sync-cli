# busmanagement/models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Bus(Base):
    __tablename__ = 'buses'
    id = Column(Integer, primary_key=True)
    capacity = Column(Integer, nullable=False)
    passengers = relationship("Passenger", back_populates="bus")

class Passenger(Base):
    __tablename__ = 'passengers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    bus_id = Column(Integer, ForeignKey('buses.id'))
    bus = relationship("Bus", back_populates="passengers")
