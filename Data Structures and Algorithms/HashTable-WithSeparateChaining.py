class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)

        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                return
        self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)

        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)

        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]
                return


t = HashTable()
t['march 6'] = 120
t['march 7'] = 78
t['march 8'] = 67
t['march 9'] = 4
t['march 17'] = 459

print(t.arr)
print(t['march 6'])
print(t['march 7'])
print(t['march 17'])

del t['march 17']
print(t.arr)
print(t['march 17'])

"""
Linear probing is another solution. it will check for
the next available location rather than chaining the values  
"""
