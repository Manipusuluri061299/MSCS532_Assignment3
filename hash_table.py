
import random


class HashTable:
    """Hash table using separate chaining and universal hashing."""

    PRIME = 1000000007

    def __init__(self, capacity=5, max_load_factor=0.75, seed=42):
        if not isinstance(capacity, int) or capacity < 1:
            raise ValueError("Capacity must be a positive integer")

        if not 0 < max_load_factor < 1:
            raise ValueError("Load factor limit must be between 0 and 1")

        self.capacity = capacity
        self.max_load_factor = max_load_factor
        self.buckets = [[] for _ in range(capacity)]
        self.size = 0

        rng = random.Random(seed)
        self.a = rng.randint(1, self.PRIME - 1)
        self.b = rng.randint(0, self.PRIME - 1)

    def _hash(self, key):
        if type(key) is not int:
            raise TypeError("Keys must be integers")

        return ((self.a * key + self.b) % self.PRIME) % self.capacity

    def _insert_without_resize(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]

        for entry in bucket:
            if entry[0] == key:
                entry[1] = value
                return False

        bucket.append([key, value])
        self.size += 1
        return True

    def insert(self, key, value):
        """Insert a key-value pair or update an existing key."""
        self._hash(key)

        index = self._hash(key)
        for entry in self.buckets[index]:
            if entry[0] == key:
                entry[1] = value
                return

        if (self.size + 1) / self.capacity > self.max_load_factor:
            self._resize()

        self._insert_without_resize(key, value)

    def search(self, key):
        """Return the value, or None if the key is missing."""
        index = self._hash(key)

        for stored_key, value in self.buckets[index]:
            if stored_key == key:
                return value

        return None

    def delete(self, key):
        """Delete a key and return True if it existed."""
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, entry in enumerate(bucket):
            if entry[0] == key:
                bucket.pop(i)
                self.size -= 1
                return True

        return False

    def _resize(self):
        """Double the capacity and rehash all entries."""
        old_buckets = self.buckets

        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_buckets:
            for key, value in bucket:
                self._insert_without_resize(key, value)

    def load_factor(self):
        return self.size / self.capacity

    def collision_count(self):
        return sum(
            max(0, len(bucket) - 1)
            for bucket in self.buckets
        )

    def __len__(self):
        return self.size


if __name__ == "__main__":
    table = HashTable()

    table.insert(101, "Policy A")
    table.insert(102, "Policy B")
    table.insert(103, "Policy C")

    print("Search 102:", table.search(102))
    print("Delete 101:", table.delete(101))
    print("Search 101:", table.search(101))
    print("Table size:", len(table))
    print("Capacity:", table.capacity)
    print("Load factor:", round(table.load_factor(), 3))
    print("Collisions:", table.collision_count())
