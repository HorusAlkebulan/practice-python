# fizz_buzz.py

def fizz_buzz(max_output_size):

    # every 3rd say fizz
    # every 5th say buzz
    # if both true, say fizz buzz
    # otherwise, say the integer
    interval_fizz = 3
    interval_buzz = 5
    output = []

    for i in range(max_output_size):
        base_one_idx = i + 1
        fizz_mod = base_one_idx % interval_fizz
        buzz_mod = base_one_idx % interval_buzz
        if fizz_mod == 0 and buzz_mod == 0:
            output.append("fizz buzz")
        elif fizz_mod == 0:
            output.append("fizz")
        elif buzz_mod == 0:
            output.append("buzz")
        else:
            output.append(str(base_one_idx))

    return output
