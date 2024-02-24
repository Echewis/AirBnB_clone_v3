#!/usr/bin/python3
"""This is a module that defines a base class
for all models in our hbnb clone"""
from sqlalchemy import Column, String, DATETIME
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
import uuid
from models import storage_type

Base = declarative_base()


class BaseModel:
    """ This is a base class for all hbnb models

    Attributes:
        id (sqlalchemy String): The BaseModel id.
        created_at (sqlalchemy DateTime): The datetime at creation.
        updated_at (sqlalchemy DateTime): The datetime of last update.
    """
    id = Column(String(60),
                nullable=False,
                primary_key=True,
                unique=True)
    created_at = Column(DATETIME,
                        nullable=False,
                        default=datetime.utcnow())
    updated_at = Column(DATETIME,
                        nullable=False,
                        default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """ This will Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for kw in kwargs:
                if kw in ['created_at', 'updated_at']:
                    setattr(self, kw, datetime.fromisoformat(kwargs[kw]))
                elif kw != '__class__':
                    setattr(self, kw, kwargs[kw])
            if storage_type == 'db':
                if not hasattr(kwargs, 'id'):
                    setattr(self, 'id', str(uuid.uuid4()))
                if not hasattr(kwargs, 'created_at'):
                    setattr(self, 'created_at', datetime.now())
                if not hasattr(kwargs, 'updated_at'):
                    setattr(self, 'updated_at', datetime.now())

    def __str__(self):
        """This will rturns a string representation of the instance"""
        return '[{}] ({}) {}'.format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ This will updates updated_at with current
        time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """ This will convert instance into dict format"""
        dct = self.__dict__.copy()
        dct['__class__'] = self.__class__.__name__
        for kw in dct:
            if type(dct[kw]) is datetime:
                dct[kw] = dct[kw].isoformat()
        if '_sa_instance_state' in dct.keys():
            del(dct['_sa_instance_state'])
        return dct

    def delete(self):
        """ This will deletes the current
        instance from the storage"""
        from models import storage
        storage.delete(self)