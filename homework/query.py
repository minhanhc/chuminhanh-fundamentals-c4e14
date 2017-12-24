from mlab import mlab_connect
from models.river import River

mlab_connect()

african_rivers = River.objects(continent = "Africa")
for african_river in african_rivers:
    print(african_river)

southAmerican_rivers = River.objects(continent = 'S. America', length__lt = 1000)
for southAmerican_river in southAmerican_rivers:
    print(southAmerican_river)
