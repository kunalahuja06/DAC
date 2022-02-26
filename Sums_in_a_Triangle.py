for _ in range(int(input())):
    n = int(input())
    li = []
    for i in range(n):
        li.append([int(i) for i in input().split()])
    
    # print(li)
    dp = []
    last_row = li[-1]
    print(last_row)

#test comment
