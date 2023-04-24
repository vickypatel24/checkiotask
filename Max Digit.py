def max_digit(value: int) -> int:
    # your code here
    b = []
    for x in str(value):
        b.append(x)
    b.sort()
    print(len(b))
    s = (b[len(b)-1])
    r = int(s)
print("Example:")
print(max_digit(10))

# These "asserts" are used for self-checking
assert max_digit(0) == 0
assert max_digit(52) == 5
assert max_digit(634) == 6
assert max_digit(1) == 1
assert max_digit(10000) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")
