# it is only used for check wheather  variable memory location is same or not

a = 21
b = "21"
print(a is b)


b = 34
c = 0
print(b is not c)

v = 45
v = '45'
c1  =  '45'
print(v is c1)
print(id(v))
print(id(c1))

g = 56
g1 = 56

print(id(g) is id(g1))
print(2 is 2)
q = 78
r = 78
print(q is r)

d = 67
h = 67
print(d is not h)










