from mongoengine import Document,StringField,IntField,BooleanField

class items(Document):
    name = StringField()
    duration = IntField()
    rented = BooleanField
