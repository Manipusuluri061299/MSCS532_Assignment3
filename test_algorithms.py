
import random
import unittest

from randomized_quicksort import randomized_quicksort
from deterministic_quicksort import deterministic_quicksort
from hash_table import HashTable


class TestSorting(unittest.TestCase):

    def setUp(self):
        self.algorithms = [
            randomized_quicksort,
            deterministic_quicksort,
        ]

    def check_sort(self, values):
        for algorithm in self.algorithms:
            with self.subTest(algorithm=algorithm.__name__):
                original = values.copy()
                result = algorithm(values)

                self.assertEqual(result, sorted(values))
                self.assertEqual(values, original)

    def test_empty(self):
        self.check_sort([])

    def test_single(self):
        self.check_sort([5])

    def test_sorted(self):
        self.check_sort(list(range(100)))

    def test_reverse(self):
        self.check_sort(list(range(100, 0, -1)))

    def test_duplicates(self):
        self.check_sort([4, 2, 4, 1, 2, 4])

    def test_all_equal(self):
        self.check_sort([7] * 100)

    def test_negative(self):
        self.check_sort([-8, 4, -2, 0, -10])

    def test_random(self):
        rng = random.Random(42)
        self.check_sort(
            [rng.randint(-1000, 1000) for _ in range(200)]
        )

    def test_randomized_multiple_runs(self):
        values = [8, 3, 7, 3, 9, 1, 5]
        for seed in range(30):
            result = randomized_quicksort(
                values, rng=random.Random(seed)
            )
            self.assertEqual(result, sorted(values))


class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.table = HashTable()

    def test_insert_search(self):
        self.table.insert(101, "A")
        self.assertEqual(self.table.search(101), "A")

    def test_update(self):
        self.table.insert(101, "A")
        self.table.insert(101, "Updated")
        self.assertEqual(self.table.search(101), "Updated")
        self.assertEqual(len(self.table), 1)

    def test_missing_key(self):
        self.assertIsNone(self.table.search(999))

    def test_delete(self):
        self.table.insert(101, "A")
        self.assertTrue(self.table.delete(101))
        self.assertIsNone(self.table.search(101))

    def test_delete_missing(self):
        self.assertFalse(self.table.delete(999))

    def test_negative_key(self):
        self.table.insert(-50, "Negative")
        self.assertEqual(self.table.search(-50), "Negative")

    def test_collision_chaining(self):
        table = HashTable(capacity=5, max_load_factor=0.99)

        # Force several integer keys into one bucket.
        target_index = table._hash(0)
        keys = []
        candidate = 0

        while len(keys) < 3:
            if table._hash(candidate) == target_index:
                keys.append(candidate)
            candidate += 1

        for key in keys:
            table.insert(key, str(key))

        self.assertEqual(table.collision_count(), 2)

        for key in keys:
            self.assertEqual(table.search(key), str(key))

    def test_resize(self):
        for i in range(100):
            self.table.insert(i, i * 10)

        self.assertGreater(self.table.capacity, 5)
        self.assertEqual(len(self.table), 100)

        for i in range(100):
            self.assertEqual(self.table.search(i), i * 10)

    def test_load_factor(self):
        for i in range(100):
            self.table.insert(i, i)

        self.assertLessEqual(
            self.table.load_factor(),
            self.table.max_load_factor
        )

    def test_invalid_key(self):
        with self.assertRaises(TypeError):
            self.table.insert("abc", 100)

    def test_empty_table(self):
        self.assertEqual(len(self.table), 0)
        self.assertIsNone(self.table.search(1))

    def test_large_dataset(self):
        for i in range(1000):
            self.table.insert(i, i + 1)

        for i in range(1000):
            self.assertEqual(self.table.search(i), i + 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
