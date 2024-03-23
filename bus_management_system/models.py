
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

class Admin(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)


class Bus(Base):
    __tablename__ = 'buses'
    id = Column(Integer, primary_key=True)
    capacity = Column(Integer, nullable=False)
    passengers = relationship("Passenger", back_populates="bus")
    users = relationship("User", back_populates="bus")

class Passenger(Base):
    __tablename__ = 'passengers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    bus_id = Column(Integer, ForeignKey('buses.id'))
    bus = relationship("Bus", back_populates="passengers")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    bus_id = Column(Integer, ForeignKey('buses.id'), nullable=True)
    bus = relationship("Bus", back_populates="users")