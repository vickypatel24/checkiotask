from collections.abc import Iterable


def compress(items: list[int]) -> Iterable[int]:
    # your code here
    # for ind, val in enumerate(items):
    #     if not ind or val != items[ind - 1]:
    #         yield val
    b = []
    for ind, x in enumerate(items):
        if not ind or x != items[ind-1]:
            b.append(x)
    return b

print("Example:")
print(list(compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0])))

# These "asserts" are used for self-checking
assert list(compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0])) == [
    5,
    4,
    5,
    6,
    5,
    7,
    8,
    0,
]
assert list(compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1])) == [1, 2, 1]
assert list(compress([7, 7])) == [7]
assert list(compress([])) == []
assert list(compress([1, 2, 3, 4])) == [1, 2, 3, 4]
assert list(compress([9, 9, 9, 9, 9, 9, 9])) == [9]
assert list(compress([9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9])) == [9, 0, 9]

print("The mission is done! Click 'Check Solution' to earn rewards!")
