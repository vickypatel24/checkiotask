def goes_after(word: str, first: str, second: str) -> bool:
    # your code here

    if first in word and second in word :
        a = word.index(first)
        b = word.index(second)
    else:
        return False 
    return (b == a+1)


print("Example:")
print(goes_after("world", "w", "o"))

# These "asserts" are used for self-checking
assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
