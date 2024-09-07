def quicksort(arr: list) -> list:

    # base case: empty
    if len(arr) == 0:
        return []

    # base case: 1 element
    if len(arr) == 1:
        return arr

    # recursive case:
    # pick pivot
    pivot_idx = len(arr) // 2

    # partition into 3 arrays
    left = []
    middle = []
    right = []
    for idx, item in enumerate(arr):
        if idx == pivot_idx:
            middle.append(item)
        elif item < arr[pivot_idx]:
            left.append(item)
        elif item > arr[pivot_idx]:
            right.append(item)
        else:
            raise ValueError("Invalid input array.")
    # recurse on sub-arrays
    sorted_left = quicksort(left)
    sorted_middle = quicksort(middle)
    sorted_right = quicksort(right)

    # combine sub-arrays in order
    sorted_full = sorted_left + sorted_middle + sorted_right

    return sorted_full
