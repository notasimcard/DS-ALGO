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
        if max_capacity <= 0 or max_capacity >= float('inf') or type(max_capacity) != int:
            raise Exception("Invalid capacity")

        # If capacity is some low number like 1 or 2,we need to adress other edge cases
        # I think initial size = 16 is a fair assumption for a hash table
        if max_capacity is None or max_capacity  < 16:
            self.capacity = 16
        else:
            self.capacity = max_capacity

        self.hash_table = [[] for _ in range(self.capacity)]
        self.load_factor = 0.75
        # Set a threshold  for resizing the hash table
        self.max_threshold = max(1, int(self.load_factor * self.capacity))

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
        self.max_threshold = max(1, int(self.load_factor * self.capacity))
        new_hash_table = [[] for _ in range(self.capacity)]
        for bucket in self.hash_table:
            if len(bucket) > 0:
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


class HashTableOpenAddressing:
    """
        Hash Table open Addressing
            - Can be done using 
                1. Linear probing
                2. Quadratic probing
                3. Double hashing
    """
    def __init__(self, max_capacity=None):
        if max_capacity <= 0 or max_capacity >= float('inf') or type(max_capacity) != int:
            raise Exception("Invalid capacity")

        # If capacity is some low number like 1 or 2,we need to adress other edge cases
        # I think initial size = 16 is a fair assumption for a hash table
        if max_capacity is None or max_capacity < 16:
            self.capacity = 16
        else:
            self.capacity = max_capacity
        self.hash_table = [None for _ in range(self.capacity)]
        self.load_factor = 0.75
        self.max_threshold = max(1, int(self.load_factor * self.capacity))
        self.current_threshold = 0

    def _hash(self, key):
        """
            Hash Function
        """
        hash = 0
        if key is None:
            raise Exception("Null Key Error")

        if type(key) is int:
            hash = abs(key)
        else:
            for char in key:
                hash += ord(char)
        return hash % self.capacity


    def insert(self, key, value): 
        if key is None:
            raise Exception("Null Key Error")

        key_value = KeyValue(key, value)
        key_hash = self._hash(key)
        probing_value = 1
        new_hash = key_hash
        tombstone_index = None
        while self.hash_table[new_hash] is not None:
            # Record the index of first tombstone
            if tombstone_index is None and self.hash_table[new_hash].key == "null":
                tombstone_index = new_hash
            #  If key is present, replace the value
            if self.hash_table[new_hash].key == key:
                break
            new_hash = (key_hash + self.linear_probing(probing_value)) % self.capacity
            probing_value += 1

        # If tombstone is found
        # Case I: loop found an empty bucket
        # Case II: loop found a matching key
        if tombstone_index:
            if self.hash_table[new_hash] is not None:
                self.hash_table[new_hash] = None
                self.current_threshold -= 1
            new_hash = tombstone_index

        # Assign new KeyValue object
        self.hash_table[new_hash] = key_value
        self.current_threshold += 1
        #  Check for threshold
        if self.current_threshold >= self.max_threshold:
            self._resize_table()
        # return key
        return key


    def print_table(self):
        for keyValue in self.hash_table:
            if keyValue:
                print(f"{keyValue.key} : {keyValue.value}")


    def linear_probing(self, probing_value):
        """
            Linear Probing.
            P(x) = ax + b, a != 0 and b = constant, b is arbitary
            To resolve clustering, GCD(a, probing_value) = 1
        """
        return 1 * probing_value


    def search(self, search_key):
        """
        returns True if found, False otherwise
        Search is complete when:
            1. matching key is found
            2. hits None
            3. loops through N times where N = length of hash table
                - ingnoring this case, as we have a load factor which makes sure we are 
                    never filling up the hash table
        """
        hash_key = self._hash(search_key)
        new_hash = hash_key
        probing_value = 1
        # Case II
        while self.hash_table[new_hash] is not None:
            if self.hash_table[new_hash].key == search_key:
                return {self.hash_table[new_hash].key : self.hash_table[new_hash].value}
            new_hash = (hash_key + self.linear_probing(probing_value)) % self.capacity
            probing_value += 1
        return None


    def remove(self, del_key):
        """
            To remove we do lazy deletion
                - we don't empty the bucket while deleting, we just replace it with a tombstone value
                - we replace tombstone, when we are inserting
        """
        hash_key = self._hash(del_key)
        new_hash = hash_key
        probing_value = 1
        while self.hash_table[new_hash] is not None:
            if self.hash_table[new_hash].key == del_key:
                # replacing key, value with tombstone values
                self.hash_table[new_hash].key, self.hash_table[new_hash].value = "null", "null"
                return {self.hash_table[new_hash].key : self.hash_table[new_hash].value}
            new_hash = (hash_key + self.linear_probing(probing_value)) % self.capacity
        return None


    def _resize_table(self):
        self.capacity = 2 * self.capacity
        self.current_threshold = 0
        self.max_threshold = max(1, int(self.max_threshold * self.load_factor))
        old_table = self.hash_table.copy()
        self.hash_table.clear()
        self.hash_table = [None for _ in range(self.capacity)]
        for keyValue  in old_table:
            if keyValue is not None:
                self.insert(keyValue.key, keyValue.value)


# Driver Code
hash_table = HashTableOpenAddressing(22020)

hash_table.insert("Jimi", "Hendrix")
hash_table.insert("Jimis", "Hendrix")
hash_table.insert("Jimi", "Hendrix Reborn")
hash_table.insert("Glass", "Animals")
hash_table.insert("Tame", "Impala")
hash_table.insert("James", "Blake")
hash_table.insert("Daft", "Punk")

print("Initial table:\n")
hash_table.print_table()
print("----------------------------------------------------------------------")
print("Search:\n")
print(hash_table.search("Daft"))
print("----------------------------------------------------------------------")
print("Remove:\n")
print(hash_table.remove("Daft"))
print("----------------------------------------------------------------------")
print("After removing:\n")
hash_table.print_table()
print("----------------------------------------------------------------------")
print("Inserting and found tombstone:\n")
hash_table.insert("Daft", "Punk")
hash_table.print_table()

# hash_table = HashTableSeperateChaining(6)
# hash_table.insert("Jimi", "Hendrix")
# hash_table.insert("Jimis", "Hendrix")
# hash_table.insert("Jimi", "Hendrix")
# hash_table.insert("Glass", "Animals")
# hash_table.insert("Tame", "Impala")
# hash_table.insert("James", "Blake")
# hash_table.insert("Daft", "Punk")

# # print(hash_table.search("Daft"))
# hash_table.print_table()
# print("----------------------------------------------------------------------")
# hash_table.remove("Daft")
# hash_table.print_table()
