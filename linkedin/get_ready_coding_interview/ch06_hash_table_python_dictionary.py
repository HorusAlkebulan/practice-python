# ch06_hash_table_python_dictionary.py


def adds_to_10(given_array):

    # 3, 4, 1, 2, 9 -> 1, 9
    # Adds to 10
    
    # iterate over array
    i = 0
    hashmap = {}
    while i < len(given_array):

        # if not in hashmap (dict)
        cur_num = given_array[i]
        if cur_num not in hashmap:
            # add to map, key = cur_num and value = 1
            hashmap[cur_num] = 1
        else:
            # if in map, increment count
            hashmap[cur_num] = hashmap[cur_num] + 1

        # get pairing (10 - cur_num)
        pairing = 10 - cur_num

        # if pairing key in hashmap and value > 0, return pairing
        if pairing in hashmap and hashmap[pairing] > 0:
            return [cur_num, pairing]
        # else: add to map with value = 0
        else:
            hashmap[pairing] = 0

        i += 1

    print("There is no pair that sums up to 10")
    return None

    # i = 0: 
        # hashmap = {}
        # cur_num = 3
        # pairing = 10 - 3 = 7
        # hashmap = {3: 1}
        # hashmap = {3: 1, 7: 0}

    # i = 1:
        # hashmap = {3: 1, 7: 0}
        # cur_num = 4
        # pairing = 6
        # hashmap = {3: 1, 4: 1, 6:0, 7: 0}

    # i = 2: 
        # hashmap = {3: 1, 4: 1, 6:0, 7: 0}
        # cur_num = 1
        # pairing = 9
        # hashmap = {1: 1, 3: 1, 4: 1, 6:0, 7: 0, 9: 0}

    # i = 2: 
        # hashmap = {1: 1, 3: 1, 4: 1, 6: 0, 7: 0, 9: 0}
        # cur_num = 2
        # pairing = 8
        # hashmap = {1: 1, 2: 1, 3: 1, 4: 1, 6: 0, 7: 0, 8: 0, 9: 0}

    # i = 3: 
        # hashmap = {1: 1, 2: 1, 3: 1, 4: 1, 6: 0, 7: 0, 8: 0, 9: 0}
        # cur_num = 9
        # pairing = 1
        # hashmap = {1: 1, 2: 1, 3: 1, 4: 1, 6: 0, 7: 0, 8: 0, 9: 1}

    # return (1, 9)



if __name__ == "__main__":

    given_array = [3, 4, 1, 2, 9]
    expected = [1, 9]
    result = adds_to_10(given_array)
    result = sorted(result)
    assert result == expected, f"result: {result}, expected: {expected}, locals(): {locals()}"

    print("All tests pass.")


    