# min chars insert to make a palindrome

# cac
#  i
#  j

# cab --> cabbac
def is_palindrome(str):
    # str = cab

    def recursive(str, i, j):
        # base case
        if i <= j:
            return True

        op_count = 0

        if str[i] != str[j]:
            # option 1: moving i++
            i += 1
            op_count += 1
            is_pal_i = recursive(str, i, j)

            # if true, we can stop??

            # option 2: moving j--
            j -= 1
            is_pal_j = recursive(str, i, j)

            # compare wanting minimum

            return False
        i += 1
        j -= 1
        return recursive(str, i, j)

    i = 0
    j = len(str) - 1
    return resursive(str, i, j)


def min_chars_palindrome(str):
    pass
    #


def is_palindrome(s):
    # Base case: if the string is empty or has one character, it's a palindrome
    if len(s) <= 1:
        return True
    # Check if the first and last characters are the same
    if s[0] != s[-1]:
        return False
    # Recur for the substring excluding the first and last characters
    return is_palindrome(s[1:-1])


# Example usage
print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))  # Output: False
