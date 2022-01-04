class Iterator:
    def __iter__(self):
        return self

    def __init__(self, length, items):
        self.limit = length
        self.counter = -1
        self.items = items

    def __next__(self):
        if self.counter < self.limit-1:
            self.counter += 1
            return self.items[self.counter]

        else:
            raise StopIteration
