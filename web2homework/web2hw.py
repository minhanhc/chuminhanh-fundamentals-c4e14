# Ex1:
#  There is no duplicate id
# id is what represents each data, similar to identity card
#
# Ex2 + 3
from mlab import mlab_connect
from models.service import Service


mlab_connect()
id_to_find = "5a3a984994802d324c463e16"
service = Service.objects.get(id =id_to_find)
print(service.name)

Service.objects(id = id_to_find).delete()
