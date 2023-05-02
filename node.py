class node:
    def __init__(self, key, require = []):
        self.key = key
        self.require = list
        pass

    def addReq(self, node):
        self.require.append(node)