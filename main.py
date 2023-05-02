import json
import node

def searchInList(db, key):
    item = None
    for i in db:
        if i.key == key:
            item = i
    return item

f = open('db.json')

db = json.load(f)

# should implement a BST on storing key terms, use list temporarily
items = []
# inserting "bigger" objects
for i in db["Terms"]:
    if not searchInList(items, i["key"]):
        items.append(node.node(str(i["key"]), i["require"]))

    for j in i["require"]:
        if not searchInList(items, j):
            items.append(node.node(str(j)))

for i in items:
    print(i)

# use graph for searching
while True:
    term = input()
    print(searchInList(items, str(term)).key)