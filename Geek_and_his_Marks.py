#code

T = int(input())
ans = [0]*T

for i in range(T):
    [N,X] = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    for x in arr:
        if x>X:
            ans[i]+=1

for a in ans:
    print(a)
