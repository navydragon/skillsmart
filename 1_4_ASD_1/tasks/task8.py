class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        # Простая хэш-функция, основанная на сумме ASCII-кодов символов строки
        hash_value = sum(ord(char) for char in value) % self.size
        return hash_value

    def seek_slot(self, value):
        index = self.hash_fun(value)
        initial_index = index

        while self.slots[index] is not None:
            index = (index + self.step) % self.size
            if index == initial_index:
                return None

        return index

    def put(self, value):
        index = self.seek_slot(value)
        if index is not None:
            self.slots[index] = value
        return index

    def find(self, value):
        index = self.hash_fun(value)
        initial_index = index

        while self.slots[index] is not None:
            if self.slots[index] == value:
                return index
            index = (index + self.step) % self.size
            if index == initial_index:
                return None

        return None