# number_placement.py


def number_placement(numbers: list, operators: list) -> str:
    # validate inputs
    if len(numbers) < 2 or (len(operators) != len(numbers) - 1):
        print(f"Invalid input params: {numbers}, {operators}")
        return None

    # use two pointer method, working ends to center
    numbers.sort()
    low_idx = 0
    high_idx = len(numbers) - 1
    operator_idx = 0
    output_ls = []
    output: str = None

    # loop until low_idx > high_idx
    while low_idx <= high_idx and operator_idx < len(operators):
        print(
            f"low_idx: {low_idx}, high_idx: {high_idx}, operator_idx: {operator_idx}, len_operators: {len(operators)}"
        )
        # iterate through operators, if < append low val, > append high val
        current_op = operators[operator_idx]
        if current_op == "<" and operator_idx == 0:
            output_ls.append(str(numbers[low_idx]))
            low_idx += 1
            output_ls.append(current_op)
            operator_idx += 1
            output_ls.append(str(numbers[high_idx]))
            high_idx -= 1
        elif current_op == ">" and operator_idx == 0:
            output_ls.append(str(numbers[high_idx]))
            high_idx -= 1
            output_ls.append(current_op)
            operator_idx += 1
            output_ls.append(str(numbers[low_idx]))
            low_idx += 1
        elif current_op == "<" and operator_idx > 0:
            output_ls.append(current_op)
            operator_idx += 1
            output_ls.append(str(numbers[high_idx]))
            high_idx -= 1
        elif current_op == ">" and operator_idx > 0:
            output_ls.append(current_op)
            operator_idx += 1
            output_ls.append(str(numbers[low_idx]))
            low_idx += 1
        else:
            raise ValueError(f"Invalid operator: {current_op}")
        output = " ".join(output_ls)
        print(f"output: {output}")

    # concat list as a string space delimited
    return output
