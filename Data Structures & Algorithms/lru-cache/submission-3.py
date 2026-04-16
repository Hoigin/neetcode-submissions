class LRUCache:

    def __init__(self, capacity: int):
        self.store = []
        self.capacity = capacity
        self.num = 0

    def get(self, key: int) -> int:
        for i in range(self.num):
            if self.store[i][0] == key:
                temp = self.store[i]
                self.store[i:-1] = self.store[i+1:]
                self.store[-1] = temp
                return self.store[-1][1]
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(self.num):
            if self.store[i][0] == key:
                temp = self.store[i]
                self.store[i:-1] = self.store[i+1:]
                self.store[-1] = [key, value]
                return 
        if self.num < self.capacity:
            self.store.append([key, value])
            self.num += 1
        else:
            self.store = self.store[1:]
            self.store.append([key, value])
