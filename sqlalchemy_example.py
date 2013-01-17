"""

SQLAlchemy

requires: sqlalchemy, psycopg2
sql, postgres, sqlite
connecting to the DB and DSNs
Django framework tightly integrated with its ORM

Modules
Install postgres: sudo apt_get install postgres
Install psycopg2: sudo easy_install sqlalchemy
    -wrapper around postgres for sqlalchemy

IRC (freenode)
#noisebridge
#plone
eleddy

"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
form sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://localhost/pyclass1', echo=True)
Base = declarative()
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

class Movie(Base):
__tablename__ = 'movies'

def add_stuff():
pass

def get_stuff():
pass

if __name__ == '__main__':
add_stuff()
get_stuff()