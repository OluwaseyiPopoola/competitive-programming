def main():
    n = int(input())

    print(comb(n, 5) + comb(n, 6) +  comb(n, 7))

def comb(n, r):

    res = 1
    denom = 1
    for i in range(1, r + 1):
        res *= (n - i + 1)
        denom *= i


    return res // denom

if  __name__ == "__main__":
    main()