from mongoengine import Document, StringField, IntField, BooleanField

class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    occupied = BooleanField()
