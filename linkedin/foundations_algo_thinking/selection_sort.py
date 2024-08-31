HR = "----------------------------------------------------------------------"
def selection_sort(xs: list):
    xs_length = len(xs)
    print(HR)
    print(f"xs = {xs}, length = {xs_length}")

    # iterate through the list, starting at idx 0
    for idx, val in enumerate(xs):
        print(f"Checking {val} at index {idx}")
        inner_min_val = val
        inner_min_idx = idx

        # cycle through rest of list (idx+1 to end) capturing the index of the minimum
        for inner_idx, inner_val in enumerate(xs[idx:xs_length]):
            if inner_val < inner_min_val:
                inner_min_val = inner_val
                inner_min_idx = inner_idx + idx
                print(f"New inner minimum {inner_min_val} at inner index {inner_min_idx}")
            else:
                print(f"No new minimum at inner index {inner_idx}")

        # if idx is the same as current index, do nothing
        if idx == inner_min_idx: 
            print("No swap needed.")
        else:
            print(f"Swap xs[{inner_min_idx}]={xs[inner_min_idx]} with xs[{idx}]={xs[idx]}")

            # otherwise, do a swap between current and new minimum index
            temp = xs[inner_min_idx]
            xs[inner_min_idx] = val
            xs[idx] = temp

        # increment outer loop

    return xs

