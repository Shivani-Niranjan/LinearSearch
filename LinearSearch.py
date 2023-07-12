array = list(map(int,input().strip().split()))
num = int(input())
count = 0
for i in array:
    if i == num:
        count+=1
print(count)