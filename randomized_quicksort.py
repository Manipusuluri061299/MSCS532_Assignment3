
import random


def randomized_quicksort(values, rng=None):
    """Sort a list using randomly selected pivots."""

    if rng is None:
        rng = random.Random()

    data = values.copy()

    def quicksort(low, high):
        while low < high:

            # Select a pivot uniformly at random.
            pivot_index = rng.randint(low, high)
            pivot = data[pivot_index]

            # Three-way partitioning.
            left = low
            current = low
            right = high

            while current <= right:
                if data[current] < pivot:
                    data[left], data[current] = (
                        data[current], data[left]
                    )
                    left += 1
                    current += 1

                elif data[current] > pivot:
                    data[current], data[right] = (
                        data[right], data[current]
                    )
                    right -= 1

                else:
                    current += 1

            # Recursively sort the smaller partition.
            # Continue with the larger partition.
            if left - low < high - right:
                quicksort(low, left - 1)
                low = right + 1
            else:
                quicksort(right + 1, high)
                high = left - 1

    quicksort(0, len(data) - 1)

    return data


if __name__ == "__main__":
    example = [8, 3, 7, 3, 9, 1, 5]

    print("Randomized:", randomized_quicksort(example))
