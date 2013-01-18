"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
"""
import csv

"""
engine = create_engine('postgresql://localhost/mytestdb', echo=True)
Base = declarative_base()
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
"""

"""
class Movie(Base):
    __tablename__ = 'movies'
"""


def add_stuff():
    pass


def get_stuff():
    pass


def get_csv():
    with open('crime.csv', 'rb') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            print row


if __name__ == '__main__':
	pass


get_csv()
#add_stuff()
#get_stuff()
