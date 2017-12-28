from mlab import mlab_connect
from models.item import items

from faker import Faker
from random import choice,randint

item_faker = Faker()

mlab_connect()

items.drop_collection()
for _ in range(20):
    item = items(name = item_faker.name(),
            duration = randint(0,30),
            rented = False
            )
    item.save()
