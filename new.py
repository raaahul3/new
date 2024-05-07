d={}
input1=[]
number=list(map(int,input("enter a number").strip().split()))
for i in number:
    c= number.count(i)
    d[i]=c
print(d)
for key, value in d.items():
    if value== 3:
        input1.append(key)
print(input1)