
#function decorator 1
def decor(fun,len):
# this MOD_FUNCTIO IS MODIFIED VERSION OF FUNCTION AREA WHICH GIVE AREA AND VOLUME ALSO
    def MOD_FUNCTIO():
        volume = len*len*len

        return volume , fun(100)
    return MOD_FUNCTIO


# this function area we want to modifiied it and want to calculate its volume also
def AREA(length=20):
    area = length*length
    return area

NEW_FUNCTION = decor(AREA , 100)
VOLUME , are = NEW_FUNCTION()
print(VOLUME)
print(are)

#SECOND FUNCTION DECORATOR 2

def decor_1(fun):
# this modifie_fun main hum getmounth function main add kar rahe hai feartures
    def modifie_fun(mounth):
        a =fun(mounth)
        print(a)

        if mounth <= 3:
            print('this is  moderatre winter ')
        elif mounth <= 6 and mounth > 3:
            print("thi is summer")
        elif mounth <= 9 and mounth > 6:
            print("this is not moderate winter ")
        elif mounth <= 12 and mounth > 9:
            print("this is goood hot food")
    return modifie_fun
# this get function i want to modified that
def getmounth(mounth):
    if mounth == 1:
        return 'january'
    elif mounth == 2:
        return 'febrauary'
    elif mounth == 3:
        return 'march'
    elif mounth == 4:
        return 'april'
    elif mounth == 5:
        return 'may'
    elif mounth == 6:
        return 'june'
    elif mounth == 7:
        return 'july'
    elif mounth == 8:
        return 'august'
    elif mounth == 9:
        return "seotember"
    elif mounth == 10:
        return "october"
    elif mounth == 11:
        return "november"
    else:
        return "DECEMBER"


updated_fun = decor_1(getmounth)
print(updated_fun(9))



# third decorator function


def store(fun):
    def mod_3():
        fun()
        print("thi is my updrate")
    return mod_3


def first():
    print('hii i m very goood')

d = store(first)
d()

# 4th function decorator in python
def decor_3():
    def mod_3(p, r ,t):
        print(simple_interst(500,20, 2))
        amount_1 = (p*r/100)**t
        return amount_1
    return mod_3

# this is function we want to decorat in python
def simple_interst(principle , rate, time):
    amount  = (principle* rate*time)/100
    return amount


g = decor_3()
value = g(500,20, 2)
print(value)

# 5th function decorator in python
def decorr(first):
    def final():
        value = first() + 100
        return value
    return final

# this is finction in which we want to decorate the function
def first():
    return 10


new_function =  decorr(first)
print(new_function())




def decor(num):
    def mod_num():
        value = num() + 100
        print(id(mod_num))
        return value

    return mod_num


def num():
    return 10


f = decor(num)
f()
print(id(f))


def fun6():
    a = 34
    c = 56
    d = a+ c
    return d
fun6()












def decorrr(ho):
    def mod_7():
        value = ho() + 10
        print("=+++++++++",id(mod_7))
        return value
    return mod_7


def gol():
    return 100
print("*********",id(gol))
gol = decorrr(gol)
print(gol())
print("h999999999",id(gol))


 #multiple decorator function multiple variation
def decor_m1(num):
    def mod_m1():
        print("*****8",id(mod_m1))
        a = num() +  10
        return a
    return mod_m1

def decor_m2(num):
    def mod_m2():
        print(id(mod_m2))
        print("#######",id(num))
        b = num() * 10
        return b
    return mod_m2

@decor_m2
@decor_m1
def num():
    return 100

print("i m the final",num())


# multiple functipon decorator

def dec(max):
    def mod_max_45():

        gcd = 2
        k =1
        max_num = max()
        while(k < max_num):
            if max_num%k ==  0:
                gcd = k

            k += 1
        return gcd
    return mod_max_45




def max(num1=100, num2= 150):
    if num1>num2:
        result = num1
    else:
        result = num2
    return result

max = dec(max)
print("i m maximun",max())

import numpy as np
a = np.array([34,56,78,90])
b = np.array([34,100,67,10])

def n_fun(arr,arr1):
    print(arr)
    print(arr1)
    l = []
    for i in range(len(arr)):
        l.append(arr[i])
    for j in range(len(arr1)):
        l.append(arr1[j])
    return l



new_list = n_fun(a,b)
print("hii i m new list", new_list)


# pasing the aaray and returning the array
def corr(arr):
    for i in range(len(arr)):
        print(arr[i])

    return arr
s = np.array([45,67,89,100])
new_arr = corr(s)
print("hii i new aer",new_arr)
# new array



def funarr():
    a = np.zeros((45,67,100))
    B = np.linspace(45,100, num = 25)







    return a , B
s , H = funarr()
print(s)
print("I AM LINSPACE", H)
# sum array and nqrt
from numpy import *
v = np.linspace(10,100,10)
print("hii i sum",sum(v))
print('hii i sum')
print('facloon i sqrt',sqrt(v))
print("hiii i m product value",prod(v))

from math import *
print(floor(34.5))
print(ceil(56.9))
print(sqrt(56.8))
print(floor(67.8))
print(factorial(67))
print("i m the power",pow(3,45))
tp = (45,67,800,100)
print(tp[0])
























