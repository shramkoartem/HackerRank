
def merge_the_tools(s, k):
    # your code goes here

    for i in range(0,len(s), k):
        a = s[i:i+k]
        print(''.join(sorted(set(a), key=a.index)))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
