def is_majority(items: list[bool]) -> bool:
    # your code here

    return items.count(True) > items.count(False)


print("Example:")
print(is_majority([True, True, False, True, False]))

# These "asserts" are used for self-checking
assert is_majority([True, True, False, True, False]) == True
assert is_majority([True, True, False]) == True
assert is_majority([True, True, False, False]) == False
assert is_majority([True, True, False, False, False]) == False
assert is_majority([False]) == False
assert is_majority([True]) == True
assert is_majority([]) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
