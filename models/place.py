#!/usr/bin/python3
""" This is Place Module for HBNB project """
from models import storage_type
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey


if storage_type == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False)
                          )


class Place(BaseModel, Base):
    """ This is the place to stay """
    __tablename__ = 'places'
    if storage_type == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref='place',
                               cascade='all, delete, delete-orphan')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False, backref='place_amenities')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """This will return a list of review instances with place_id"""
            from models import storage
            all_revs = storage.all(Review)
            Listz = []
            for revz in all_revs.values():
                if revz.place_id == self.id:
                    Listz.append(revz)
            return Listz

        @property
        def amenities(self):
            """ Thi will return the list of Amenity instances
                based on the attribute amenity_ids
            """
            from models import storage
            all_amens = storage.all(Amenity)
            Listz = []
            for amen in all_amens.values():
                if amen.id in self.amenity_ids:
                    Listz.append(amen)
            return Listz

        @amenities.setter
        def amenities(self, Objectz):
            """This ia the method that will add an Amenity.id to the
                attribute amenity_ids
            """
            if Objectz is not None:
                if isinstance(Objectz, Amenity):
                    if Objectz.id not in self.amenity_ids:
                        self.amenity_ids.append(Objectz.id)
