# 100 doors, starting as closed (closed=0, open=1) or (closed=False, True)
# step = 1 first pass
# every step, toggle (if 0 set to 1 and 1 to 0)
# IDEA: would binary operations helpful here
# brute force seem like effectively n * n = n ** 2, can we do better?


def flip_doors(num_doors: int):

    # initial setup
    door_state: list = [False] * num_doors
    big_o_count = 0

    # loop through step values
    for step in range(1, num_doors + 1):

        # loop through doors using step value (account for zero base)
        start = step - 1
        for i in range(start, num_doors, step):

            # flip door
            # door_state[i] = (True if door_state[i] == False else False)
            door_state[i] = not door_state[i]
            big_o_count += 1

    print(f"big_o_count: {big_o_count}, door_state: {door_state}")
    return door_state
