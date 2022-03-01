# Day 13
# Problem 13
# Date 22 Feb 2022
# Time 7:20 PM

# input -> s = "abcba"
#       -> k = 2
# output -> "bcb"

def get_substring(s, k):

    if not s:
        return ""
    elif len(s) <= k:
        return s
    elif k == 1:
        return s[0]

    unique_char = 0
    checked_chars = set()
    c = None
    rem = None

    first_char = s[0]
    second_char_index = 0

    while s[second_char_index] == first_char:
        second_char_index += 1

    c = s
    for index, char in enumerate(s):
        if char not in checked_chars:
            checked_chars.add(char)
            unique_char += 1
        if unique_char > k:
            c = s[:index]
            rem = s[second_char_index:]
            break

    longest_rem = get_substring(rem, k)

    longest_substring = None
    if len(c) < len(longest_rem):
        longest_substring = longest_rem
    else:
        longest_substring = c
    return longest_substring


print(get_substring("abcba", 2))
