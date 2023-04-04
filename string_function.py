
# converting the lower case
st = "I AM SIDDHARTH KUMAR SHARMA"
ST1 = st.lower()
print(ST1)

# converting the upper case
ST3 = "i am siddahrth kumar sharma"
st4 = ST3.upper()
print(st4)

# converting the swapecase
a = "i am Siddharth Kumar Sharma"
B = a.swapcase()
print(B)


# title the number
SID = ST3.title()
print(SID)

G = "i m blessed and universe will me to make possible to what i actually want to do"
g1 = G.title()
print(g1)


# using the method islower , isupper , istitle
text1 = "HFYRFGBHBG"
TEST1 = text1.islower()
print(TEST1)
#
#
#
TEXT2 = "gffgbfvgfbghfb"
TEST2 = TEXT2.isupper()
print(TEST2)
#
Text3 = "I Am Blessed"
test3 = Text3.istitle()
print(test3)
#
# # string method is isdigit , isalpha , isalnum
text5 = "123487544"
value = text5.isdigit()
print(value)
#
text6 = "rhfgngvbhnv"
value2 = text6.isalpha()
print(value2)

text7 = "hgrhvbriuif468F*%#"
value3 = text7.isalnum()
print(value3)
#
text8 = "hfhgnf"
value_1 = text8.isalpha()
print(value_1)

text9 =  "bggbgbuhfggb8776"
value7 = text9.isalnum()
print(value7)

TEXT10  = "hii i m very cool "
value = TEXT10.rstrip()
print(value)





# using replace function
str_ch = "finding nether land "
new = str_ch.replace("nether","emmo")
print(new)


str_n = "i m very cool boy"
str = str_n.replace("i","heyy")
#print(new)
print(id(str_n))
#print(id(new))
print(str_n)
print(str)
print(id(str_n))
print(id(str))

# split() method in string
words = "finding-the nemo netherland i m  also provide to find the path"
new_str = words.split(" ")
print(new_str)


word1 = "gfbgh,gnn,  gjjg,jhgtjguj,ngtjhguj"
new_list = word1.split(",")
print(new_list)




# join function in string
l = ["i","am very good","therefore","i amblessed"]
new_string =" ".join(l)
print(new_string)
set ={"jgj","hgh","fhhh","huhrg"}
new = "*".join(set)
print(new)
print(type(new))




l1 = ["gool", "hfhg","34","jggm","678"]
new_str = " ".join(l1)
print(new_str)

l2 = ["uhfuh","fhbgb","nfgubnu","hruhuhu"]
new_str2 = "$".join(l2)
print(new_str2)
j = "jfjf"
h = "jfjgj"
b = "*".join(j)
print(b)


# startswith() and endswith() method in string
str_val = "i guys the universe is helping me to reality whT I AM REALLY WANT TO DO"
CHECK = str_val.startswith("i guys")
print(CHECK)


str_val_1 = "hellow guys chai piloo"
check_1 = str_val_1.endswith("i piloo")
print(check_1)



            







































