from typing import List


class OrderedStream:
    def __init__(self, n: int):
        self._arr = [''] * (n + 1)
        self._cur = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self._arr[idKey] = value
        res = []
        while self._cur < len(self._arr) and self._arr[self._cur] != '':
            res.append(self._arr[self._cur])
            self._cur += 1
        return res


s = OrderedStream(5)
print(s.insert(3, 'ccccc'))
print(s.insert(1, 'aaaaa'))
print(s.insert(2, 'bbbbb'))
print(s.insert(5, 'eeeee'))
print(s.insert(4, 'ddddd'))
