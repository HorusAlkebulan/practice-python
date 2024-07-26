string1 = "mississippi"
string2 = "mossyistheapple"
# max_substring = ""

# string1 = "mississippi"
# string2 = "mossyistheapple"
# max_substring = ""

def maximal_substring(string1, string2):
    # the idea: use recursion
    max_substring = recurse_maximal_substring(string1, string2, 0, 0, "", "")
    return max_substring
    
def recurse_maximal_substring(string1, string2, string1_idx, string2_idx, substring, max_substring):
    # string1_idx = 0
    # string2_idx = 0 
    # substring = ""

    # base case: empty string
    # if len(substring) == 0:
    #     return ""

    # base case: chars at both indexes equal (found a match)
    # return substring + matched_char
    # if string1[string1_idx] == string2[string2_idx]:
    #     return substring + string1[string2_idx]

    # base case: beyond EOS for either
    # return substring
    if string1_idx == len(string1) or string2_idx == len(string2):
        if len(substring) > len(max_substring):
            max_substring = substring
        return max_substring

    # recursive case: iterate through string1 chars, starting with current idx1, holding string2_idx steady
    #   if find char match, 
    #       shrink the window by 1 and recurse again with match char added
    #       if substring found is bigger, set as new max
    #       break out of the loop
    for idx in range(string1_idx, len(string1)):
        if string1[idx] == string2[string2_idx]:
            cur_substring = recurse_maximal_substring(string1, string2, idx + 1, string2_idx + 1, substring + string1[idx], max_substring)
            if len(cur_substring) > len(max_substring):
                max_substring = cur_substring
            break

    # recursive case: same as above, but string2
    for idx in range(string2_idx, len(string2)):
        if string2[idx] == string1[string1_idx]:
            cur_substring = recurse_maximal_substring(string1, string2, string1_idx + 1, idx + 1, substring + string2[idx], max_substring)
            if len(cur_substring) > len(max_substring):
                max_substring = cur_substring
            break

    # recursive case: finally, if match not found, 
    #   recurse again, incrementing both idx, but recurse without adding char
    cur_substring = recurse_maximal_substring(string1, string2, string1_idx + 1, string2_idx + 1, substring, max_substring)
    if len(cur_substring) > len(max_substring):
        max_substring = cur_substring
    return max_substring

result = maximal_substring(string1, string2)
print(f"result: {result}")
