# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
from collections import Counter

if __name__ == "__main__":
    instring = ""
    for line in sys.stdin:
        instring += line
    n_shoes, sizes, n_cust, *buys = instring.split("\n")
    
    n_shoes = int(n_shoes)
    sizes = Counter(sizes.split(" "))    
    n_cust = int(n_cust)
    tran = [x.split(" ") for x in buys ]

    cash = 0    
    for i in tran:
        if sizes[i[0]] > 0:
            cash += int(i[1])
            sizes[i[0]] -= 1

    print(cash)
