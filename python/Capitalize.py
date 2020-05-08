# Complete the solve function below.
def solve(s):
    s = s.title()
    s = [s[0]]+[s[i+1].lower() if s[i].isdigit() else s[i+1] for i in range(len(s)-1) ]
    return "".join(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
