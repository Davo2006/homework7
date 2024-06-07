#xndir3.py ( Write a program to check if two strings are balanced)
s1 = "Yn"
s2 = "PYnative"
y = True
for i in s1.lower():
    if i not in s2.lower():
        y = False
print(y)
