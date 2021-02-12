##sorted
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

print(sorted(student_tuples, key= lambda x: x[1]))

##fibonacci sum decorator
import functools
def lru_cache(f):
    cache = {}
    @functools.wraps(f)
    def wrapper(v):
        if v in cache:
            return cache[v]
        out = f(v)
        cache[v] = out
        return out
    return wrapper

@lru_cache
def fib(n: int):
    """Computes the Fibonacci number at index n"""
    if n<2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(100))
print(help(fib))

##Class decorator
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print('Hello')

say_hello()
say_hello()

##Iterables
#Para que sea un iterable debe implementar el método __iter__, el cual retorna un iterator. 
#Incluso si aún no sabemos qué es un iterator, 
#sabemos que podemos obtener uno si le pasamos un iterable a la función iter
class StudentNames:
    def __init__(self, names):
        self._names = tuple(names)
    
    def __iter__(self):
        return iter(self._names)

names = StudentNames(["Sebastian", "Pepito", "Pablito"])
for n in names:
    print(n)

##Generators, memory efficent
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
    
for c in reverse("Python"):
    print(c)

obj = reverse("The best class ever")
next(obj), next(obj)

#Memory efficient
import sys
mygenerator = (i for i in range(100000) if i % 2 == 0)
print(sys.getsizeof(mygenerator))

mylist = [i for i in range(100000) if i % 2 == 0]
print(sys.getsizeof(mylist))
