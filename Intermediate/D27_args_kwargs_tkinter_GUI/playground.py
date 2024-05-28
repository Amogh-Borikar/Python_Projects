# *args example
def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)

add(1, 1 , 2, 3, 4, 5, 6, 9, 10)


# **kwargs example
class car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = car(make="nissan")
print(my_car.make)