from .. import db, ma
from abc import abstractmethod
from sqlalchemy.sql import functions

class Base(db.Model):
    __abstract__ = True

    update_date = db.Column(db.DateTime(), nullable=True)
    delete_date = db.Column(db.DateTime(), nullable=True)
    create_date = db.Column(db.DateTime(), server_default=functions.current_timestamp(), nullable=False)

    @abstractmethod
    def select_all(self, *args, **kwargs):
        """select all"""
        raise NotImplementedError()

    @abstractmethod
    def select_id(self, *args, **kwargs):
        """select by id"""
        raise NotImplementedError()

    @abstractmethod
    def create(self, *args, **kwargs):
        """create"""
        raise NotImplementedError()

    @abstractmethod
    def update(self, *args, **kwargs):
        """update"""
        raise NotImplementedError()



class BaseSchema(ma.Schema):
    class Meta:
        model = Base
        ordered = True