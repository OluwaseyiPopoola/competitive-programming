def main():
    n = int(input())

    for _ in range(n):
        a, b = input().split()

        val = kmp_search(a, b)
        if len(val):
            print(len(val))

            for _ in range(len(val)):
                print(val[_] + 1, end=" ")
            print()
        else:
            print("Not Found")




def compute_lps(pattern):
    m = len(pattern)
    lps = [0]*m
    length = 0
    i = 1
    

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)

    i = 0
    j = 0
    matches = []

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            matches.append(i - j)
            j = lps[j - 1]

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches


            





        


    


if __name__ == "__main__":
    main()