# Complete the function/method (depending on the language) to return true/True when
# its argument is an array that has the same nesting structures and same corresponding
# length of nested arrays as the first array.

# For example:

# # should return True
# same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# # should return False
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# # should return True
# same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# # should return False
# same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )


def same_structure_as(original, other):
    if type(original) is not list and type(other) is not list:
        return True
    elif type(original) is not list or type(other) is not list:
        return False

    if len(original) != len(other):
        return False

    for orig, oth in zip(original, other):
        if not same_structure_as(orig, oth):
            return False

    return True
