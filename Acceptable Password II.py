def is_acceptable_password(p: str) -> bool:
    b = [x for x in range(10)]
    n = 0
    for z in p :
          for y in b :
           if str(y)==z :
            n = 1
            break

    if len(p)>6 and n ==1 :
       return True
    else :
       return False
         
            


print("Example:")
print(is_acceptable_password("short"))

# These "asserts" are used for self-checking
assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == False
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")