def add_me(a, b):
 return a+b
def subtract_me(a, b):
 return a-b


for el in dir():
    if el[0:2] != "__":
        del globals()[el]
print(dir())