
def deterministic_quicksort(values):
    """Sort values using the first element as pivot."""
    data = values.copy()

    def sort(low, high):
        while low < high:
            pivot = data[low]
            lt, i, gt = low, low, high

            while i <= gt:
                if data[i] < pivot:
                    data[lt], data[i] = data[i], data[lt]
                    lt += 1
                    i += 1
                elif data[i] > pivot:
                    data[i], data[gt] = data[gt], data[i]
                    gt -= 1
                else:
                    i += 1

            # Recurse on the smaller partition.
            if lt - low < high - gt:
                sort(low, lt - 1)
                low = gt + 1
            else:
                sort(gt + 1, high)
                high = lt - 1

    sort(0, len(data) - 1)
    return data


if __name__ == "__main__":
    example = [8, 3, 7, 3, 9, 1, 5]
    print("Deterministic:", deterministic_quicksort(example))
