import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds117010.mlab.com:17010/fordatabse

# host is address of database
host = "ds117010.mlab.com"
# port is the gate to each room of data
port = 17010
# db_name is the name of databse
db_name = "fordatabse"
user_name = "gottenvn"
password = "Tung11112010"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())