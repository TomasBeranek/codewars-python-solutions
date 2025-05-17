# Create a function that takes a positive integer and returns the next bigger
# number that can be formed by rearranging its digits. For example:

#   12 ==> 21
#  513 ==> 531
# 2017 ==> 2071

# If the digits can't be rearranged to form a bigger number, return -1
# (or nil in Swift, None in Rust):

#   9 ==> -1
# 111 ==> -1
# 531 ==> -1


def next_bigger(n):
    s = list(str(n))

    for i, digit in enumerate(reversed(s), start=1):
        min_bigger_suffix_digit = min(
            [d for d in s[-i:] if d > digit], default=-1)
        if min_bigger_suffix_digit != -1:
            res = list(s)
            res[-i] = s[s.index(min_bigger_suffix_digit)]
            suffix = res[-i+1:]
            suffix.append(digit)
            suffix.remove(min_bigger_suffix_digit)
            min_suffix = sorted(suffix)
            res[-i+1:] = min_suffix
            return int(''.join(res))

    return -1
