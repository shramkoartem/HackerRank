# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

for a in sys.stdin:
    s = a

n, m = [int(a) for a in s.split(" ")]

dot = ".|."


for i in range(0,int(n/2)):
    print(((1+i*2)*dot).center(m,"-"))

print("WELCOME".center(m, "-"))

for i in range(int(n/2),0,-1):
    print(((i*2-1)*dot).center(m,"-"))
