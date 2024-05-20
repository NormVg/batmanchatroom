from tinydb import TinyDB,Query,where
import tinydb
db =  TinyDB("./db/db.json")

person = tinydb.Query()

db.insert({'username': 'tippo', 'password': "32a912105fd4928bfd348b38ccc7ab3123c228d2e27e3e5e5ef5442db5286310"})
db.insert({'username': 'vishnu', 'password': "7fe017a59440c783fabc539c5697ab9b7fce16deb0865826ab6bcf25e22bbce5"})
print(db.all())

# [
#     {"msg":"hello","by":"Norm","time"}
# ]