S = int(input())
num_array = list(map(int, input().split()))
l1 = []
for i in range(S):
    l1.append(0)
l2 = []
for i in range(S):
    l2.append(0)
for i in range (S) :
    l1[num_array[i]-1] = i+1

for i in range (S) :
    l2[l1[i]-1] = i+1

if l2[i] != num_array[i] :
    print("IMPOSSIBLE")
else :
    for i in range(S):
        print(l1[i], end=" ")