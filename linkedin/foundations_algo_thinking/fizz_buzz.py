# fizz_buzz.py

def fizz_buzz(max_output_size):

    # every 3rd say fizz
    # every 5th say buzz
    # if 15th, say fizz buzz
    # otherwise, say the integer
    interval_fizz = 3
    interval_buzz = 5
    interval_fizz_buzz = 15
    output = []

    for i in range(max_output_size):
        base_one_idx = i + 1
        if base_one_idx % interval_fizz_buzz == 0:
            output.append("fizz buzz")
        elif base_one_idx % interval_fizz == 0:
            output.append("fizz")
        elif base_one_idx % interval_buzz == 0:
            output.append("buzz")
        else:
            output.append(str(base_one_idx))

    return output
