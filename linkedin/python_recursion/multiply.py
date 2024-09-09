# multiply.py


def multiply(multiplier: int, multiplicand: int):
    # base case
    if multiplicand == 1:
        return multiplier

    # movement to base case
    multiplicand -= 1

    # combine results
    product = multiplier + multiply(multiplier, multiplicand)

    return product
