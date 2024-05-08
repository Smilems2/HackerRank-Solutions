n, m= map(int, input().split())
Arr=map(int, input().split())
A=set(map(int, input().split()))
B=set(map(int, input().split()))
score=0
for i in Arr:
    if i in A:
        score+=1
    if i in B:
        score-=1
print(score)