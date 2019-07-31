class Storage(object):
    def __init__(self, dimension):
        self.dimension = dimension
        self.data = dict()
        
    def keys(self):
        return self.data.keys()
        
    def clear(self):
        self.data.clear()
        
    def __getitem__(self, key):
        if not key in self.data: self.data[key] = self.createDefault()
        return self.data[key]
        
    def __setitem__(self, key, value):
        if value == None:
            self.data[key] = ""
            del self.data[key]
        else:
            self.data[key] = value

    def createDefault(self):
        if self.dimension <= 1:
            return self.createDefaultValue()
        else:
            return Storage(self.dimension - 1)
