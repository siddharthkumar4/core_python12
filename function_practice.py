




def add():
    a = 34
    b = 89
    c= a+b
    print(c)
add()

def subtraction():
    x = 56
    y = 67
    c = x*y
    print(c)
subtraction()

#returning the grade
def grade(marks):
    if marks>=90:
        print("this marks is first class",marks)
    elif marks >80 and marks<90:
        print("this marks is second class",marks)
    elif marks >70 and marks <80:
        print("this marks is 3rd",marks)
    else:
        print("u r pivit try next time")

grade(77)
grade(0)
#
for i in range(10):
    marks = int(input("enter"))
    grade(marks)


# function returning the only ine value
def DI(R,Y):
    G = R/Y
    return G
S,R,Y = DI(34,6)
print(S)
print(R)
print(Y)

def main():
    d = DI(50,5)*7
    print(d)

main()
#

def fun(w,r,t):
    final = (w+r+t)/4
    return w,r,t,final
x,y,z,fial_value =  fun(60,89,78.9)
print(x)
print(y)
print(z)
print(fial_value)

def ABC(R,U,I,O):
    return (R+U+I+O)/4,R,U,I,O
D,X,Y,Z,S = ABC(56,78,90,10)
print(D)
print(X)
print(Y)
print(Z)
print(S)

# nested function
def first_char():
    def second():
        print("i m the first function ")

    second()
    print("hii i m hte first chareacter")




first_char()


def first1():

    def second():

        print("hii i second")
    second()
    print("hii i first")



print("hii i outside")
first1()

def myfirst(a,b):
    c = a+b
    def mysecond():
        g = c*10
        return g
    return c , mysecond()

x , y = myfirst(10,5)
print(x)
print(y)


#finding the gratest number
def max(num1, num2):
    if num1>num2:
        print(num1)
        max_num = num1
    else:
        print(num2)
        max_num = num2
    return max_num


def main(x,y):
    gt = max(x,y)
    print("this is the great number", gt)



main(45,67)
main(600,1)


def DI(V,U,I):
    result = V*(U+I)
    def DI1():
        result2 = result/5
        return result2
    DI1()

    return DI1()
A = DI(45,70,1)
print("this is the fucking value",A)


def SI(P1,R1,T1):
    amount = (P1*R1*T1)/100
    P2 = P1
    R2 = R1
    T2 = T1
    def CI(P2,R2,T2):


        amount2 = ((P1*R1)/100)**T1
        return amount2

    return CI(P2,R2,T2), amount

FINAL_ci,final_SI= SI(70,10,90)
print("THIS IS CI ",FINAL_ci)
print("THIS IS SI",final_SI)


def st():
    return "ankit", 'siddharth'
first1 , second2 = st()
print('this is my first strinf',first1)
print("this is my second string",second2)




def hii():
    print("i m very cool boy")
    def jack():
        print('hii i am very blessed')
    jack()



hii()

# taking function as as the argument
def room(fu):
    return "i m very cool boy" + fu()
def cell():
    return "45566"
a = room(cell)
print(a)

def gool(para):
    return "&&&&&&&&&&&&" + para()
def foom():
    return "*************"


value = gool(foom)
print(value)
# taking two function as the argument
def calc(a ,b):
    total = a() + b()
    return total

def circle():
    x = 25
    area = 22/7*(x*x)
    return area
def square():

    x = 25
    area1 = x*x
    return area1



total_area = calc(circle,square)
print("this is the total area", total_area)

def york():
    return 56
def uk():
    return 56
def sum(a,b):
    value = a() +b()
    return value

value = sum(york,uk)
print("this is my vlaue",value)


# function returning another function
def vi(bi):
    return bi
def bi():
    return "huhgoigiotnibntignn"

h = vi(bi)
print(h())

# increament value
def increment(x):
    x+=1
    return x

def ask_me(y):
    inc = increment(y)
    return inc
d =   ask_me(45)
print(d)

def ti(f):
    print("hii i m good")
    return f
def fii():
    print("hii i m very")



d = ti(fii)
d()



# returning the another function by the function which is inside the function
def gool():
    print("hiii i m outter function")
    def jack():
        print("hi i m inner function")
    return jack
f = gool()
f()

# returning the function which is outside the function


def figure(fun):
    return fun
def square():
    length = 5
    area = 5*5
    return area
final_fun  = figure(square)
print(final_fun())




















































