from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session
from datetime import datetime
import quake


### Code for creating the database
# python -i model.py
# engine = create_engine("sqlite:///terranote.db", echo=True)
# Base.metadata.create_all(engine)


engine = create_engine("sqlite:///terranote.db", echo=False)
session = scoped_session(sessionmaker(bind=engine,
                                      autocommit = False,
                                      autoflush = False))

Base = declarative_base()
Base.query = session.query_property()

### Class declarations go here
class Quake(Base):
    """ from quake.py """  
    __tablename__ = "quakes"

    # id = Column(Integer, primary_key = True)
    event_id = Column(String(50), unique=True, primary_key = True)
    depth = Column(String(25), nullable = False)
    title = Column(String(400), nullable = False)
    quake_type = Column(String(25), nullable = False)
    magnitude = Column(String(10), nullable = False)
    place = Column(String(500), nullable = False)
    coordinates = Column(List, nullable = False)
    latitude = Column(Float, nullable = False)
    longtitude = Column(Float, nullable = False)
    time = Column(DateTime, nullable = False)
    url = Column(String, nullable = False)
    seismictype = Column(String, nullable = False)
    status = Column(String, nullable = False)
    tsunami = Column(Integer, nullable = False)
    felt = Column(Integer, nullable = False)
    recordtime = Column(DateTime, nullable = False)

### End class declarations

def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///terranote.db", echo=True)
    Session = sessionmaker(bind=ENGINE)

    return Session()

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()

