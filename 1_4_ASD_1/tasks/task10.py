class PowerSet:

    def __init__(self):
        self.storage = []

    def size(self):
        return len(self.storage)

    def put(self, value):
        if value not in self.storage:
            self.storage.append(value)

    def get(self, value):
        return value in self.storage

    def remove(self, value):
        if value in self.storage:
            self.storage.remove(value)
            return True
        return False

    def intersection(self, set2):
        result = PowerSet()
        for value in self.storage:
            if set2.get(value):
                result.put(value)
        return result

    def union(self, set2):
        result = PowerSet()
        for value in self.storage:
            result.put(value)
        for value in set2.storage:
            result.put(value)
        return result

    def difference(self, set2):
        result = PowerSet()
        for value in self.storage:
            if not set2.get(value):
                result.put(value)
        return result

    def issubset(self, set2):
        for value in set2.storage:
            if not self.get(value):
                return False
        return True


