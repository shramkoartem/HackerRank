def minion_game(string):
    consonants = "bcdfghjklmnpqrstvwxyz".upper()
    letters = list(string)
    n = len(letters)
    
    stuart = []
    kevin = []
    
    stuart = ["".join(letters[i:j]) for i in range(n) for j in range(i, n+1) if len(letters[i:j]) and "".join(letters[i:j])[0] in consonants ]
    kevin = ["".join(letters[i:j]) for i in range(n) for j in range(i, n+1) if len(letters[i:j]) and "".join(letters[i:j])[0] not in consonants ]
    
    stuart = list(set(stuart))
    kevin = list(set(kevin))
    
    
    s_score = sum(count_substring(string, sub) for sub in stuart)
    k_score = sum(count_substring(string, sub) for sub in kevin)
    
    if s_score > k_score:
        return print("Stuart "+str(s_score))
    elif s_score == k_score:
        print("Draw")
    else:
        return print("Kevin "+str(k_score))
    
def count_substring(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count


if __name__ == '__main__':
    s = input()
