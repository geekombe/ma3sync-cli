
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

engine = create_engine('sqlite:///bus_management.db')
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

from .models import Base, Admin
from sqlalchemy.exc import IntegrityError

def init_db():
    Base.metadata.create_all(bind=engine)
    session = Session()
    try:
        session.add(Admin(username="admin", password="1234"))
        session.commit()
    except IntegrityError:
        session.rollback()
