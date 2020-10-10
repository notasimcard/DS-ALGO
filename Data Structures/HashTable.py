# TODO: Implement hash table with Open Addressing

# Key Value pair object that goes into the table
class KeyValue:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __eq__(self, other):
        return self.key == other.key


class HashTableSeperateChaining:
    # Initializing max capacity of Hash Table
    def __init__(self, max_capacity=None):
        if max_capacity is None:
            self.capacity = 16
        else:
            if max_capacity < 0 or max_capacity > float('inf'):
                raise Exception("Invalid capacity")
            self.capacity = max_capacity

        self.hash_table = [[] for _ in range(self.capacity)]
        self.load_factor = 0.75
        # Set a threshold  for resizing the hash table
        self.max_threshold = int(self.capacity * self.load_factor)
        self.current_threshold = 0

    def _hash(self, key):
        hash = 0
        if key is None:
            raise Exception("Null Key Error")
        
        if type(key) == int:
            hash = abs(key)
        else:
            for char in key:
                hash += ord(char)
        return hash % self.capacity


    def insert(self, key=None, value=None, dict_like_iterable=None):
        if dict_like_iterable is not None:
            for item in dict_like_iterable:
                self.insert(item.key, item.value)
            return
        key_hash = self._hash(key)
        new_entry = KeyValue(key, value)
        
        for key_value in self.hash_table[key_hash]:
            if key_value == new_entry:
                return

        # Seperate Chaining
        self.hash_table[key_hash].append(new_entry)

        self.current_threshold += 1
        # Check if we reached our max threshold
        if self.current_threshold >= self.max_threshold:
            self._resize_table()


    def remove(self, del_key):
        del_key_hash = self._hash(del_key)
        for index, key_value in enumerate(self.hash_table[del_key_hash]):
            if key_value.key == del_key:
                self.hash_table[del_key_hash].pop(index)
                return


    def search(self, find_key):
        key_hash = self._hash(find_key)
        for key_value in self.hash_table[key_hash]:
            if find_key == key_value.key:
                return key_value.value
            else:
                return None


    def _resize_table(self):
        print("Threshold reached. Resizing table.....")
        print("----------------------------------------------------------------------")
        print("Before resizing\n")
        self.print_table()
        self.capacity = 2 * self.capacity
        self.max_threshold = self.capacity * self.load_factor
        new_hash_table = [[] for _ in range(self.capacity)]
        for bucket in self.hash_table:
            for key_value in bucket:
                new_hash_table[self._hash(key_value.key)].append(key_value)
        
        self.hash_table.clear()
        self.hash_table = new_hash_table.copy()
        print("\n After resizing\n")
        self.print_table()
        print("----------------------------------------------------------------------")

        return


    def print_table(self):
        for bucket in self.hash_table:
            if len(bucket) > 0:
                for item in bucket:
                    print(f"{item.key} : {item.value}")
                print("-----")

hash_table = HashTableSeperateChaining(6)


hash_table.insert("Jimi", "Hendrix")
hash_table.insert("Glass", "Animals")
hash_table.insert("Tame", "Impala")
hash_table.insert("James", "Blake")
hash_table.insert("Daft", "Punk")

# print(hash_table.search("Daft"))
hash_table.print_table()
print("----------------------------------------------------------------------")
hash_table.remove("Daft")
hash_table.print_table()
