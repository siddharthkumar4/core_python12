l1 = [45,67,89,"siddharth"]
print(l1[3][0:5:2])
# scling the list
print(l1[-1:-3:-1])
print(l1[-1:-5:-2])
print(l1[-1:-4])
print(l1[0:6])
print(l1[0:4:2])
l = [1,2,3,4,5,6,7,89,0]
print(l[0:2])
print(l[0:3])
print(l[0:5])
print(l[0:6])
print(l[0:7:2])

# acessing the list
l3 = [34,"hjj", 56,78,100, 400]
print(l3[0])
print(l3[2])


# modifying the list l3
l3[0] = 45
l3[1] = 100
l3[2] = 300
print(l3)
l3[4] = 45
l3[5] = 100
print(l3)
print(l3[0])
print(l3)

# accessing the list through lopp
for i in l3:
    print(i)
j = 0
# accesing the loop through while loop
while(j<len(l3)):
    print("i m new",j,l3[j])
    j+=1

# passing the list in lambda
s = lambda l3: print(l3)
s(l3)

s = lambda h,k : (h+k)**2
print(s(45,67))

# appending the blank list
# l = []
# n = int(input("enter the number"))
# for i in range(n):
#     l.append(int(input("enter the number")))
#
# for j in l:
#     print(j)

# slicing the list
s = [23,45,100,1,50,100,70]
print(s[0:5])
for i in s[0:5]:
    print(i)

# allicsing comment
s = [34,100,44]
d = s
print(d)
print("allissing",id(d))
print("alliisng ",id(s))

# changing the list
s[0] = 10
print(s)
print(d)

s[0] = 56
print(s)
print(d)
print(id(d))
print(id(s))
s[1] = 400
print(s)
print(d)
# insert method
l = [45,'sid', 900, 800,100]
l.insert(2,49)
print(l)
lm = l
lm.insert(3,0)
print(lm)
print(l)
print(78)


# insert() method
# h = [34,56,100,600,1]
# h.pop()
# print("fucj",(h))
# h.pop(2)
# print(h)
# print(h.pop(3))
# removing the list
list = [23,56,100,56]
i

print(list)
# reverse the method
list_3 = [34,56,89,90]

list_3.reverse()

print("hii i am here",list_3)
print("hii iam ", list_3)
print("google",list_3)

list_3.reverse()
print(list_3)
list_3.reverse()
lj=[34,56,78,100]
lk = [34,100,45,78]
new_list = lj.extend(lj)
print(new_list)



# method in count functionn
a = [3456, 78,90]
k = a.count(783)
print(k)

g = [78,90,100,89]
g.sort()
g.clear()
print("hii i am g",g)




j = [56,78,34]
h = [45,100,67]
h.extend(j)
print(h)
g_1 =(56,89)
l.extend(g_1)
print("hii i am very cool",l)

# scillising the array
ja = [45,100,78,67,90]
ha = ["gh",89,100,78,100,6]
g = ja + ha
print("i m the rweal g",g)

f = [[3455,78],[100,67,3,9],[23,907]]
print(f[0][0])
print(f[0][1])





l8 = [34,89,100,56]
print(l8[-1:-3:-1])
print(l8[1:7])
print(l8[1:4])
print("************",l8[-1:-3:-1])

print("yyyyyyyyyy",l8[-3:-1:-1])

l4 = [[34,56],[10,10]]
l4 = [[45,67],[10,5,90]]
print(l4)


l_9 = [23,67,90,100,78,100,5]
print("g0000000",l_9[6::-1])

j = [45,100,56,2,8,40]

j = [45,67,100,[34,1,4,80]]
print("i m the list",j[3][3:0:-1])




s = [23,56,90,100,78,3,9]
print(s[-4::-1])

#allising the list
g = [4,89,56,90]
h = g
print(id(g))
print(id(h))
print(id(h))


# copy method on list
k = [45,89,100,56,56]
s = k.copy()
k[0] = 78
print(k[0])
print(k)
print(k[0])
print(s)

# coloning the list
j = [56,100,3,50]
c = j[:]
print("hii i am clone",c)
c[0] = 7
j[0] = 30
print(c)
print(j)



# nested th list
r = [[34,67],[100,56,89],[89,56,10,100]]
print(r[0])
print(r[1])
h = [[56,89],[0,78,100,0,[46,89,0]]]
print(h[1][4][0])

#print(h[5])
j = [[45,78,100,67],[34,100,100,88]]
k = [[34,100,67,10],[2],[34,[19.90,[12,45,90]]]]

#print(k[2][1][0][])

h = [[34,56,78],[2],[23,10,[1,34,56,89]]]
print(h[2][2][0])
j = [[23,45,100,45],
     [89,100,78,10]]

#print(j[0][4])

# nnested list
list_final_0 = [(23,45,67,100),[12,45,78,90,[45,89,100]]]
print(list_final_0[0][0:3])
print(len(list_final_0))





# accessing the  nested list by while
def fun_list(list):

    i = 0
    while (i < len(list)):
        if type(l[i]) == list:
            j = 0
            while (j < len(list[i])):
                print(j[i][0], end=" ")
                j += 1
        else:
            print(list[i], end=" ")

        i += 1


k = [34,67,89,[1,45,78]]
k = [78,90,1,4,78,[12,67,90]]
fun_list(k)



# accessing the nested list by loop
def jack(haary):
    i = 0
    while(i<len(haary)):
        if type(haary[i]) == list:
            j = 0
            while(j<len(list[i])):
                print(haary[i][j],end =  " ")
                j+=1
        else:
            print(haary[i],end=" ")
        i+=1
new_liat = [34,78,0,3,[34,78,100]]

jack(new_liat)

print()



h_1 = [12,45,56,[12,45,100],[1,9000,56,789,90]]
i = 0
while(i<len(h_1)):
    if type(h_1[i]) == list:
        j = 0
        while(j<len(h_1[i])):
            print(h_1[i][j], ends =" ")

            j+=1
    else:
        print(h_1[i], end= " ")
    i+=1

print()

list_g = [[1,2,3,4,5],[6,7,8,9,0]]

print(len(list_g))
def nested_list(list):
    i = 0
    j = 0
    while(i<len(list)):
        j = 0
        while(j<len(list[i])):
            print("hiii i m",i,j,list[i][j])
            j+=1
        i+=1

list_1 = [[1,2,3,4,5],[6,7,8,9,67]]
list_4 = [[34,78,100],[1,809,0]]
print(nested_list(list_4))


# list function


# 2nd dimension
list_0 = [[1,2,3,4,5],
        [12,23,34,40,50],
        [0,9,8,7,1,34],
          [1,20,45,80,100,0]]
print(list_0[1][0:4])

print(list_0[2][0:4])

list_set = [[1,2,3,4,5],
            [12,4,5,78,8],
            [34,5,6,10,100],
            [1,67,90,45,10]]

print(list_set[1:2][0:2])



kj = [[1,2,3,45,5],[67,89,100,8],[23,5,89,100],[45,78,0,3]]
print("i m one two dimension",kj[0:3])
print("i m two dimension",kj[0:1][0:2][0:2])
print("i m three dimensuuion",kj[0:1][0][0:2])
print("i m three dimension")


print(kj[0:1][0])



v = [[23,45,6,7,89],[12,3,4,78,90],(12,34,45,67,78)]



print(v[2:3])
print(v[1:2][0:1])
print(v[0:1][0][0:3][0])

h = [45,78,90]
print(h[0:1][0])

j = list("siddharth")
print(j)













































