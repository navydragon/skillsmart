class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        sum_ = 0
        for char in key:
            sum_ += ord(char)
        return sum_ % self.size

    def is_key(self, key):
        index = self.hash_fun(key)
        return self.slots[index] == key

    def put(self, key, value):
        index = self.hash_fun(key)
        self.slots[index] = key
        self.values[index] = value

    def get(self, key):
        index = self.hash_fun(key)
        if self.slots[index] == key:
            return self.values[index]
        return None
