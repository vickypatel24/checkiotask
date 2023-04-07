from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # your code here
        s = 0
        for x in elements:
            if x != elements[0]:
                s = s+1
        if s==0 :
            return True
        else:
            return False
        


print("Example:")
print(all_the_same([1, 1, 1]))

# These "asserts" are used for self-checking
assert all_the_same([1, 1, 1]) == True
assert all_the_same([1, 2, 1]) == False
assert all_the_same([1, "a", 1]) == False
assert all_the_same([1, 1, 1, 2]) == False
assert all_the_same([]) == True
assert all_the_same([1]) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
