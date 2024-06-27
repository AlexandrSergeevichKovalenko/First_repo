'''a = input("Enter the number: ")
a = int(a)
if (a== 0):
    print("zero")
elif (a>=10 and a<100):
    print("ok")
else:
    print("pp")
'''
'''
name = input("Enter name: ")
if name:
    print(f"Hi {name}")
else:
    print("anonimus")
'''
'''name = "Sasha"
age = int(input("Enter your age: "))
has_driver_license = input(" ")
if name and age >=18 and has_driver_license:
    print(f"{name} take your car")
else:
    print("fuck off")
'''
'''
a = -5
b = -7

res = abs(a) if a > b else abs(b)
print(res)
'''

'''if a > b:
    res=a
else:
    res = b
print(res)
'''

'''
s = "python"
t = "upper"

res = s.upper() if t == "upper" else s
print(res)
'''
'''a = 12
b = 7'''
'''
[1, 2, a if a<b else 3, 4, b if b>a else a, 6]
'''

'''
"a - " + ("even" if a % 2 == 0 else "odd") + "number"

'''
'''
max (1, 5, a if a>0 else b, 4, 6 )
'''

'''
a = 2
b = 3
c = 4

d = (a if a>c else c) if a>b else (b if b>c else c)
print (d)
'''

'''
if x>= 0
    if y >= 0:
        print("quater f ")
    else:
        print("quatert u ")
else:
    if y>=0:
        print("quater r ")
    else:
        print("quater c ")
'''
'''
fruit = "apple"
for char in fruit:
    print(char)
'''


'''
i = -1
N = -10
while i > N:
    print(i)
    i *= 2
    '''
'''
pass_true = "password"
ps = ""

while ps != pass_true:
    ps = input ("enter the pasword")

print("Yoor password is correct")
'''

'''
N = 20
i = 1

while i <= N:
    if i%3 == 0:
        print (i)
    
    i+=1
'''

'''
d = [1, 5, 3, 6, 0, -4]

flFind = False
i = 0
while i < len(d) and d[i] % 2 != 0:
    i += 1
if flFind:
        break
'''

'''
flFind = i != len(d)

print(flFind)
'''
'''
s = 0
d = 1

while d != 0:
    d = int(input("enter any integer value"))
    if d % 2 == 0:
        continue

    s +=d
    print("s = " + str (s))
'''

'''
s = 0
i = -10

while i < 100:
    if i == 0:
        break
    s+= 1/i
    i += 1

else:
    print("the suum is correct")
print(s)
'''

'''
d = [1,2,3,4,5]

for x in d:
    print(x)
    '''

# char = "python"

# for x in char:
  #      print(x)

#d = [1,2,3,4,5]

#p = 1
#for x in d:
  #  p *=x

#print (p)

#a = 0
#while a < 6:
  #  a +=1
   # if a%2 == 0:
   #     continue
    #print(a)

'''
d = [1,2,3,4,5]

for i in range(len(d)):
    d[i] = 0

print(d)

s = 0
for i in range(2,1001):
    s+=1/i
print(s)
'''
 
'''
pass_true = "password"
ps = ""

while ps != pass_true:
   ps = input("enter the password: ")

print("password was entered successfully.")
'''

'''
N = 20
i = 1

while i <= N: 
    if i%3 == 0: 
        print(i)
    i += 1
'''

'''
i = 100
N = 999
while i <= N:
    if i%47 == 43 and i%3==0:
        print (i)
    i+=1
'''

# print ("start")


'''
d = [1,3,5,6,0,-4]

flFind = False
i = 0
while i < len(d):
    print(i)
    flFind = d[i] % 2 == 0
    if flFind :
        break
    i+=1
print(flFind)
'''

'''
s = 0
d = 1

while d != 0:
    d = int(input("enter the integer value: "))
    if d% 2 == 0:
        continue
    s += d
    print("s = " + str (s))
    '''

""" s = 0
i = -10

while i < 10:
    if i == 0:
        break
    s += 1/i
    i += 1
else:
    print("correct")

print(s)
"""

'''
["Moscow", "Twer", "Vologda"]
'''
'''
marks = [2, 3, 4, 3, 5, 2]

min(marks)

sum(marks) / len(marks)

sorted(marks)

marks_sorted = sorted (marks)

marks_sorted = sorted(marks, reverse=True)
'''
'''
s = list('python')
print(s)
'''

'''
t = [1, 2, 3, 'RTTYUI', "holla"] 
del t [0]
print(t)
'''



'''
p = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
i = 0
summ_P = 0

while summ_P <= 5:
    summ_P = int(sum(p))
    if summ_P == 5:
        break
    i = int(input("Enter the number: "))
    if p[i] > 0:
        continue
    p[i] = 1
print (*p)
'''

'''d = [1,2,3,4,5,6,7]

for i in d:
    print(i)
'''
'''
d = [1, 2, 3, 4, 5]
6
for i in range (0, len(d), 3):
    d[i] = 0
print(d)    
'''

'''
a = list(range(11))
print(*a)
'''

'''
a = list(range(1, 20, 3))
print(*a)
'''
'''
summ = 0
entered_List = input().split()
num_List =[int(i) for i in entered_List]
for i in num_List:
    if i%2 == 0:
        continue
    summ += i
print(summ)
'''

'''
n = int(input("Enter the value: "))

if n < 1 or n > 100:
    print("there value does not belong to the range")

else:
    p = 1
    for i in range(1, n+1):
        p *= i
    print(f"Factorial {n} = {p}")

'''

'''
for i in range(7, 1, -1):
    print("*" * i)
'''
'''
words = [ "Python", "give", "me", "strengs", "to", "sucseed", "on", "this", "course"]

s = ""

'''
'''
for w in words:
    s+= " " + w
print(s.lstrip()) 
'''
'''
print(" ".join(words))
'''

'''
digs = [4, 3, 100, -53, -30, 1, 34, -8]
'''

'''
for i in range(len(digs)):
    if digs[i] >= 10 or digs[i] <= -10:
        digs[i] = 0
'''
    
'''for i, d in enumerate(digs):
    if 10 <= abs(d) <= 99:
        digs[i] = 0
print(digs)
'''

'''
name = input("What is your name >>>")
age = int(input("What is your age >>>"))

message = f"Hallo Mr: {name} {age}"
print(message)

print("*" * 10)

'''
'''
age = int(input("age>>"))
hour = int(input("What is an hour>>"))
have_id = bool(int(input("do youn have ID card (1 -yes, 0 - no>>>)")))

condition = (age >= 18 and have_id) or hour == 21

if (condition):
    print("it is allow for you to drink alcochol")
else:
    print("younare too young")

    
    '''


"""
message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""

for ch in message:
    if ch.isalpha():
        position = ord(ch.lower()) - ord('a')
        encoded_position = (position + offset) % 26
        encoded_char = chr(encoded_position + ord('a'))
        if ch.isupper():
            encoded_char = encoded_char.upper()
        encoded_message += encoded_char 
    else:
        encoded_message += ch
"""

result = None
operand = None
operator = None
wait_for_number = True

while True:
    operand = float(input("Enter the operand"))
    






















