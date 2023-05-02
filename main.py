import json
import node

def searchInList(l, key):
    for i in l:
        if i is isinstance(i, node.node) and i.key == key:
            return True

    return False

f = open('db.json')

db = json.load(f)

# should implement a BST on storing key terms, use list temporarily
items = []
for i in db["Terms"]:
    for j in i['require']:
        if searchInList(db, j) is False:
            items.append(node.node(j))

for i in items:
    print(i.key)

# use graph for searching