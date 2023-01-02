m = input()
m = m.split(" ")
n = m[1]
m = m[0]
def domino(x, y):
    print(((int(x)*int (y))/2))
domino(m, n)