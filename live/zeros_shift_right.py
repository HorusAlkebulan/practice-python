# Eg) I/P - [1,8,0,0,7,0,4,5]
#              i
#                j


def shift_zeros_right(arr: list) -> list:

    i = 0

    while i < len(arr) - 1:  # i = 0, 1

        # increment until next val is either 0 or end of list
        if arr[i + 1] == 0:  # arr[i + 1] = 8, 0

            # find next non-zero, starting with i+1
            j = i + 1  # j = 2
            while j < len(arr) and arr[j + 1] == 0:  # j = 3, arr[4] = 7

                # keep looking
                j += 1  # j = 3

            # swap value in i and j place
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

            # move index to value after the swapped in zero
            i = j + 1
        else:
            # simple increment
            i += 1  # i = 1

    return arr
