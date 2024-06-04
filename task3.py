def main():
    meets = []
    n = int(input())
    for i in range(n):
         meets.append([int(i) for i in input().split()])
    meets.sort(key=lambda x: x[1] - x[0])
    times=set()
    meets_count = 0
    busy = 0
    for i in meets:
        for j in range(i[0], i[1]):
            if j in times:
                busy = 1
        if not busy:
            meets_count += 1
            [times.add(i) for i in range(i[0], i[1])]
        busy = 0
    meets.sort(key=lambda x: x[1])
    print(meets_count, meets[-1][1])

main()