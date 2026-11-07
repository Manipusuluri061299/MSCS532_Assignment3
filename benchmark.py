
import csv
import random
import statistics
import time

from randomized_quicksort import randomized_quicksort
from deterministic_quicksort import deterministic_quicksort
from hash_table import HashTable


SIZES = [100, 500, 1000, 2000]
REPEATS = 5


def create_data(size, data_type):
    rng = random.Random(42 + size)

    if data_type == "random":
        return [rng.randint(0, size * 10) for _ in range(size)]

    if data_type == "sorted":
        return list(range(size))

    if data_type == "reverse":
        return list(range(size, 0, -1))

    if data_type == "repeated":
        return [rng.randint(0, 9) for _ in range(size)]

    raise ValueError("Unknown dataset type")


def benchmark_sort(algorithm, values, randomized=False):
    durations = []

    expected = sorted(values)

    for trial in range(REPEATS):
        rng = random.Random(100 + trial)

        start = time.perf_counter()

        if randomized:
            result = algorithm(values, rng=rng)
        else:
            result = algorithm(values)

        elapsed = time.perf_counter() - start

        assert result == expected
        durations.append(elapsed * 1000)

    return statistics.median(durations)


def run_sort_benchmarks():
    rows = []

    algorithms = [
        ("Randomized Quicksort", randomized_quicksort, True),
        ("Deterministic Quicksort", deterministic_quicksort, False),
    ]

    for size in SIZES:
        for data_type in (
            "random", "sorted", "reverse", "repeated"
        ):
            values = create_data(size, data_type)

            for name, algorithm, is_randomized in algorithms:
                elapsed_ms = benchmark_sort(
                    algorithm, values, is_randomized
                )

                row = {
                    "algorithm": name,
                    "size": size,
                    "dataset": data_type,
                    "median_time_ms": round(elapsed_ms, 4),
                }

                rows.append(row)
                print(row)

    with open(
        "benchmark_results.csv",
        "w",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=rows[0].keys()
        )
        writer.writeheader()
        writer.writerows(rows)

    print("\nSorting benchmarks completed.")
    print("Results saved to benchmark_results.csv")


def run_hash_analysis():
    print("\nHash Table Load Factor and Collision Analysis")

    rows = []

    for count in [10, 100, 500, 1000]:
        # Use a large initial table to study load factor
        # without automatic resizing during insertion.
        table = HashTable(
            capacity=2003,
            max_load_factor=0.99,
            seed=42,
        )

        rng = random.Random(100 + count)
        keys = rng.sample(range(1000000), count)

        start = time.perf_counter()

        for key in keys:
            table.insert(key, key * 2)

        insertion_ms = (time.perf_counter() - start) * 1000

        for key in keys:
            assert table.search(key) == key * 2

        row = {
            "entries": count,
            "capacity": table.capacity,
            "load_factor": round(table.load_factor(), 4),
            "collisions": table.collision_count(),
            "total_insert_time_ms": round(insertion_ms, 4),
        }

        rows.append(row)
        print(row)

    with open(
        "hash_results.csv",
        "w",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=rows[0].keys()
        )
        writer.writeheader()
        writer.writerows(rows)

    print("\nHash analysis completed.")
    print("Results saved to hash_results.csv")


if __name__ == "__main__":
    run_sort_benchmarks()
    run_hash_analysis()
