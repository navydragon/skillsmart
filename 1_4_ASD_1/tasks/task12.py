class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def _hash(self, key):
        """Внутренний метод хэширования"""

        return hash(key) % self.size

    def _find_slot(self, key):
        """Внутренний метод поиска слота для ключа"""

        index = self._hash(key)
        for _ in range(self.size):
            if self.slots[index] is None or self.slots[index] == key:
                return index
            index = (index + 1) % self.size
        return None

    def _evict_least_used(self):
        """Внутренний метод вытеснения наименее используемого элемента"""

        min_hits = min(self.hits)
        index = self.hits.index(min_hits)
        self.slots[index] = None
        self.values[index] = None
        self.hits[index] = 0

    def put(self, key, value):
        """Добавляет или обновляет значение в кэше, вытесняя наименее используемый элемент при необходимости"""
        index = self._find_slot(key)
        if index is None:
            self._evict_least_used()
            index = self._find_slot(key)
        self.slots[index] = key
        self.values[index] = value
        self.hits[index] = 0

    def get(self, key):
        """Возвращает значение по ключу и увеличивает счётчик обращений"""
        index = self._hash(key)
        for _ in range(self.size):
            if self.slots[index] == key:
                self.hits[index] += 1
                return self.values[index]
            if self.slots[index] is None:
                return None
            index = (index + 1) % self.size
        return None