#xndir2.py ( Count all letters, digits, and special symbols from a given string)
x = "P@#yn26at^&i5ve"
y = 0
t = 0
u = 0
for i in x:
    if i.upper().isupper():
        y+=1
    elif i.isdigit():
        t+=1
    else:
        u+=1
print("chars =",y)
print("digits =",t)
print("symbols =",u)

