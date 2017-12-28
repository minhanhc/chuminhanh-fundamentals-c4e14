from mlab import mlab_connect
from models.item import items

mlab_connect()

renteds = items.objects(duration__gt = 0)
for rented in renteds:
    if rented.rented is False:
        rented.update(set__rented = True)
