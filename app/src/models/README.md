# model


## Usage

[base.py](https://github.com/beerjoa/flask-restplus-skeleton/tree/master/app/src/models/base.py)

```python
from .. import db, ma
from sqlalchemy.sql import functions

class Base(db.Model):
    __abstract__ = True

    update_date = db.Column(db.DateTime(), nullable=True)
    delete_date = db.Column(db.DateTime(), nullable=True)
    create_date = db.Column(db.DateTime(), server_default=functions.current_timestamp(), nullable=False)


    def select_all(self, *args, **kwargs):
        pass

    def select_id(self, *args, **kwargs):
        pass

    def create(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        pass



class BaseSchema(ma.Schema):
    class Meta:
        model = Base
        ordered = True
```