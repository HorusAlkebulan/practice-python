def make_change(amount: float):
    # given values of 
    # 1, 2, 5, 10, 20, 50p
    # 1, 2 pounds
    denominations = {
        0.01: "1p",
        0.02: "2p", 
        0.05: "5p",
        0.10: "10p",
        0.20: "20p",
        0.50: "50p",
        1.00: "1q",
        2.00: "2q",
    }
    denomination_values = [
        2.00,
        1.00,
        0.50,
        0.20,
        0.10,
        0.05,
        0.02, 
        0.01,
    ]
    change_remaining = amount
    results = []

    for denomination_value in denomination_values:

        # get quotient for this denom value using floor division
        quotient = int(change_remaining // denomination_value)
        if quotient > 0:
            denomination_total = quotient * denomination_value
            change_remaining -= denomination_total
            denomination_name = denominations[denomination_value]
            results.append(f"{quotient}x{denomination_name}")
        # otherwise skip this denom

    return results