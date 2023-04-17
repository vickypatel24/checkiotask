def follow(instructions: str) -> tuple[int, int] | list[int]:
    # your code here
    a = 0
    b = 0
    for x in instructions:
        if x == "f":
            a +=1
        elif x == "b":
            a -=1
        elif x == "l":
            b-=1
        elif x =="r":
            b+=1

    return (b, a)


print("Example:")
print(list(follow("fflff")))

# These "asserts" are used for self-checking
assert list(follow("fflff")) == [-1, 4]
assert list(follow("ffrff")) == [1, 4]
assert list(follow("fblr")) == [0, 0]

print("The mission is done! Click 'Check Solution' to earn rewards!")
