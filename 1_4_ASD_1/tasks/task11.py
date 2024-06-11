class BloomFilter:
    def __init__(self, size=32):
        self.size = size
        self.bit_array = 0

    def hash1(self, string):
        hash_value = 0
        for char in string:
            hash_value = (hash_value * 17 + ord(char)) % self.size
        return hash_value

    def hash2(self, string):
        hash_value = 0
        for char in string:
            hash_value = (hash_value * 223 + ord(char)) % self.size
        return hash_value

    def add(self, string):
        hash1 = self.hash1(string)
        hash2 = self.hash2(string)
        self.bit_array |= (1 << hash1)
        self.bit_array |= (1 << hash2)

    def is_value (self, string):
        hash1 = self.hash1(string)
        hash2 = self.hash2(string)
        return (self.bit_array & (1 << hash1)) and (self.bit_array & (1 << hash2))



