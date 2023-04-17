def checkio(array: list[int]) -> int:
   # your code here
   if len(array)>0:
       l = (array[len(array)-1])
       n = 10
       s=0
       for x in array :
           if n %2==0:
               s = s + x        
           n = n+1
       return s*l
   else:
       return 0


print("Example:")
print(checkio([0, 1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert checkio([0, 1, 2, 3, 4, 5]) == 30
assert checkio([1, 3, 5]) == 30
assert checkio([6]) == 36
assert checkio([]) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
