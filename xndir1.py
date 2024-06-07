#xndir1.py ( Arrange string characters such that lowercase letters should come first)
x = "pyNaTivE"
y = ''
f = ''
for i in x:
    if i.isupper():
        y+=i
    else:
        f+=i
f +=y
print(f)
x = x.replace("py","xy")
print(x)