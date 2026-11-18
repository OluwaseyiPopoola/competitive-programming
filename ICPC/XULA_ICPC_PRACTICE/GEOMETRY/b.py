def main():
    n, d = list(map(int, input().split())) 
    m = int(input())
    for _ in range(m):
        x, y = list(map(int, input().split()))

        state = False

        if (y >= ((-1*x) + d)) and (y >=( x - d)) and (y <=( x + d)) and (y <= ((-1*x) + (2*n) - d)):
            state = True


        val = "YES" if state else "NO"
        print(val)


if __name__ == "__main__":
    main()