import sys
test_cases=int(sys.stdin.readline()) # 4
tc=list(map(int,sys.stdin.readline().split(' '))) # [1,3,5,7]

cnt=0
for n in tc:
    if n==1: continue
    elif n==2:
        cnt+=1
        continue
    elif n%2==0:
        continue
    for i in range(3,n,2):
        if n%i==0:
            break
    else:
        cnt+=1

print(cnt)