size = input()
size = size.split(' ')
y = size[0]
n = size[1]
if type(y) is not int:
    y = int(size[0])
if type(n) is not int:
    n = int(size[1])    

if (y and n):
    print((y * n) // 2)