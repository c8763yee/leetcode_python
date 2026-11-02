class RandomizedSet:

    def __init__(self):
        self.set = {}
        self.index_list = []
        self.length = 0

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        
        self.set[val] = self.length
        self.index_list.append(val)
        self.length += 1
        return True

    def remove(self, val: int) -> bool:
        # Example(val = 7)

        # before
        # [3,7,5,6,4]
        # {3: 0, 7: 1, 5: 2, 6: 3, 4: 4}

        # after
        # [3, 4, 5, 6]
        # {3: 0, 4: 1, 5: 2, 6: 3}
        if val not in self.set:
            return False

        # change value of last index in set to val's index
        index_of_removed_element = self.set[val] 
        self.set[self.index_list[-1]] = index_of_removed_element 
        
        # swap removed_element and last_element in index_list, then pop last element of it
        self.index_list[-1], self.index_list[index_of_removed_element] = self.index_list[index_of_removed_element], self.index_list[-1]
        self.index_list.pop()
        del self.set[val]
        self.length -= 1
        return True
        

    def getRandom(self) -> int:
        return self.index_list[int(random.random()*len(self.index_list))]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()