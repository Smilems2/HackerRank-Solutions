n=int(input())
A=set(map(int, input().split()))
m=int(input())
B=set(map(int, input().split()))
r=(A.union(B)-A.intersection(B))
m=list(r)

for i in sorted(m):
    print(i)
s