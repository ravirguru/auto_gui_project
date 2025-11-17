from re import match


def fly():
    print("All birds can fly")


class Bird:
    pass

class Penguin(Bird):
    print("Penguins cant fly")

def make_bird_fly(bird):
    bird.fly()

b = Bird()
#make_bird_fly(b)
p = Penguin()
#make_bird_fly(p)



items=["A",1,"C",2,"B",3]

from collections import  Counter

count = Counter(items)
print(count)

print(dict(sorted(zip(items[::2], items[1::2]))))

# print(items[::2])
# print(items[1::2])

#(r"![\d.]")


def find_num(a,b,c):
    match True:
        case _ if a >= b and a >= c:
            greatest = a
        case _ if b >= c:
            greatest = b
        case _:
            greatest = c
    return greatest

print(find_num(10,20,22))



a= 20
b=30
c=40
greatest2 = a if a > b and a > c else (b if b > c else c)
print(greatest2)

a =90
b = 100
c = 200

greatest3 = a if a > b and a > c else ( b if b > c else c)
print(greatest3)

