class DynamicArray:
    def __init__(self, capacity=8):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * self.capacity

    def insert(self, value, index):
        if self.count == self.capacity:
            # TODO: INCREASE SIZE
            print("ERROR ARRAY IS FULL")
            return
        # Check if we are at capacity / not intalized with a value
        if index >= self.count:
            # TODO: better error handling
            print("ERROR INDEX OUT OF BOUNDS")
            return
        # Create more space in the array. shift the data one value at a time
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i - 1]  # goto the end of the array and assign a value to it

        self.storage[index] = value
        self.count += 1

    def append(self, value):
        # Check if we are at capacity
        if self.count == self.capacity:
            print("ERROR: Array is full")
            return

        self.count += 1
        # -1 is to account for 0 index
        self.storage[self.count - 1] = value

    def double_size(self):
        self.capacity *= 2
        # Create a new array that is double in size
        new_storage = [None] * self.capacity
        # fill the new array with the old data
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        # change the pointer to the new array, old storage is now garbage and gets collected
        self.storage = new_storage
