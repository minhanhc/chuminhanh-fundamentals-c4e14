import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds135519.mlab.com:35519/a-task-v2

host = "ds161426.mlab.com"
port = 61426
db_name = "wwinter"
user_name = "admin"
password = "admin"


def mlab_connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
