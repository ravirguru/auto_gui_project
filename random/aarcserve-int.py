# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#prime nos...
#int - input
#o/p - check for bool True or False.
#program1
def is_prime(n: int):
    return not any ( n % i == 0 for i in range(2, n))

print(is_prime(7))
print(is_prime(70))
print(is_prime(2))

#program2
s1="this is a test"
# op=[h,a,e]
from collections import Counter

count = Counter(s1)
result = { k:v for k,v in Counter(s1).items() if v==1}
print(list(result)) # ['h', 'a', 'e']

