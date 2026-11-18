def main():
    t = int(input())

    for _ in range(t):
        points = []
        for _ in range(3):
            points.append(list(map(int, input().split())))

        points.sort(key = lambda x: x[1])

        res = 0

        if points[-1][1] == points[-2][1]:
            res  = dist(points[-1], points[-2])

        print(res)


def dist(p1, p2):
    return ((p1[0] -p2[0])**2 + (p1[1] - p2[1])**2)**0.5


if __name__ == "__main__":
    main()