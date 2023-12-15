import ast
from graphviz import Digraph as dgph
from IPython.display import Image
from pprint import pprint

def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def difference(a,b):
    return abs(a-b)

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b


for i in range(11):
    print(multiplication(i,2))