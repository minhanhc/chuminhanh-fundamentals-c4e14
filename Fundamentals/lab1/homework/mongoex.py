from pymongo import MongoClient

client = MongoClient("mongodb://admin:admin@ds021182.mlab.com:21182/c4e")

db = client.get_default_database()

posts = db['posts']

new_post = {
    'title': "Unnamed song",
    'author': "Anonymous",
    'content': '''Where we have been, let it stay for now
    How we have been, let it stay for now
    Youth is the memory and vice versa
    That year of the boy and the girl
    Were their eyes connected deeply'''
}

posts.insert_one(new_post)

customers = db['customers'].find()
count = {
    'count_wom': 0,
    'count_ads': 0,
    'count_events': 0
}
for customer in customers:
    if customer['ref'] == 'wom':
        count['count_wom'] += 1

    elif customer['ref'] == 'ads':
        count['count_ads'] += 1

    elif customer['ref'] == 'events':
        count['count_events'] += 1

print("# of customers by ads: ", count['count_ads'])
print("# of customers by events: ", count['count_events'])
print("# of customers by wom: ", count['count_wom'])

for key,value in count.items():
    percent = round(value * 100 /6969,2)
    print(key,percent)

from matplotlib import pyplot
labels = ['ads','events','wom']
colors = ['red','blue','yellow']
data = [27.81,55.96,16.23]

pyplot.pie(data, labels = labels, colors = colors)
pyplot.axis('equal')
pyplot.show()
