"""
Input:

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Output:

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""


def wrap(string, max_width):
    s = list(string)
    m = max_width+1
    for i in range(m-1,len(string)+m, m):
        s.insert(i, "\n")
    return ''.join(s)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
