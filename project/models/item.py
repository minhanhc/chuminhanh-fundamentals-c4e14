from mongoengine import Document,StringField,IntField,BooleanField
from mlab import mlab_connect

class items(Document):
    name = StringField()
    duration = IntField()
    rented = BooleanField()
