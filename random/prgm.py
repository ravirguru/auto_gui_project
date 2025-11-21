from time import sleep

#palidrome
res = lambda s: bool(s and s.strip())  and (s == s[::-1])
print(res("raccar"))

#fibonacci series.
def fibo_check(n: int) -> list:
    if n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        series = fibo_check(n-1)
        series.append(series[-1] + series [-2])
    return series

print(fibo_check(10))

#reversing string without inbuilt methods.
def _reverse(any_string):
    li = []
    for i in range(len(any_string)-1,-1,-1):
        li.append(any_string[i])
    return "".join(li)
print(_reverse("Hello"))

#prime nos.
def is_prime_no(n):
    return  not any (n % i == 0 for i in range(2, int(n**0.5) + 1))

# return not any (n % i ==0 for i in range(2, int(n**0.5) + 1))
# for prime nos, use generator expression  ()
# (  n % i ==0  for i in range(2, int(n**0.5)+1))
print(is_prime_no(18))

def _is_prime(n):
    return  not any (n % i == 0 for i in range(2, int(n**0.5) + 1))

import re
s1 = "finding email address abc@gmail.com"
res = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+$", s1)
print(res)


s3 = "racecar"

is_pal = s3 == s3[::-1]
print(is_pal)


def rotate_left(li : list, n) -> list:
    return  li[n:] + li [:n]

print(rotate_left(["Cat","rat","dog","bird"],3))


arr =  [11, 2, 9, 18, 15, 5, 3, 4, 6, 9]

target = 20
pairs = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr [j] == target:
            pairs.append((arr[i], arr[j]))
print(pairs)

from collections import Counter
arr2 = [11,1,33,7,10,2,3,9,45,7,5]

count = Counter(arr2)
pairs2 = set()
target = 12

for num in arr2:
    complement = target - num
    #Special case: if num == complement, ensure at least two occurrences
    if count[num] > 0 and count[num] == 2:
        continue
    pairs2.add(tuple(sorted((num,complement)))) # here sorted((num,complement)) is one argument taking as tuple itself.
print(pairs2)

from selenium import  webdriver

driver = webdriver.Chrome()

driver.switch_to.new_window("window")
driver.get_screenshot_as_png()
sleep(5)
driver.get("https://amazon.in")
driver.maximize_window()
sleep(5)

words1 = ["look","into","my","eyes","look","into","my","eyes","look","into","my","eyes"
         "not", "around", "the", "eyes", "not", "around", "the", "eyes"]
words ="RAADDDDDDOOOOO"
from collections import  defaultdict

d = defaultdict(int)

for word in words:
    d[word] += 1
print(d)

res = sorted(d.items(), key= lambda item: item[-1])
print(res)

def count_items_in_list(li: list) -> dict:
    d = {}
    for item in li:
        d[item] = d.get(item,0) + 1
    return  d
sorted_item = sorted(d, key=lambda x: x[-1])
print(sorted_item)

print(count_items_in_list(['a','b','a','c','a','e','b']))