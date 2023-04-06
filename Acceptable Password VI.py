# Taken from mission Acceptable Password V

# Taken from mission Acceptable Password IV
# Taken from mission Acceptable Password III
# Taken from mission Acceptable Password II
# Taken from mission Acceptable Password I
def is_acceptable_password(p: str) -> bool:
    # your code here
    b = [x for x in range(10)]
    n = 0
    f = p.find("password")
    F = p.find("PASSWORD")
    for z in p :
          for y in b :
           if str(y)==z :
            n += 1
    if len(p) > 9 and f<0 and F <0 and len(set(p)) > 2:
       return True
    elif len(p)>6 and n !=0 and n!=len(p) and f<0 and F <0 and len(set(p)) > 2:
      return True
    else :
      return False


print("Example:")
print(is_acceptable_password("short"))

# These "asserts" are used for self-checking
assert is_acceptable_password("short") == False
assert is_acceptable_password("short54") == True
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False
assert is_acceptable_password("12345678910") == True
assert is_acceptable_password("password12345") == False
assert is_acceptable_password("PASSWORD12345") == False
assert is_acceptable_password("pass1234word") == True
assert is_acceptable_password("aaaaaa1") == False
assert is_acceptable_password("aaaaaabbbbb") == False
assert is_acceptable_password("aaaaaabb1") == True
assert is_acceptable_password("abc1") == False
assert is_acceptable_password("abbcc12") == True
assert is_acceptable_password("aaaaaaabbaaaaaaaab") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
