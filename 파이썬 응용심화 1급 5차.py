# 문제 1

'''
rtey
n=int(input())
s=[]
cnt=0

s.append([0])

while len(s)!=0:
    x=s.pop()
    
    if sum(x)==n:
        cnt+=1
    elif sum(x)<n:
        s.append(x+[1])
        s.append(x+[2])
        s.append(x+[3])

print(cnt)
'''

# 문제 2

'''
walls=[[1,4],[2,6],[3,5],[5,3],[6,2]]
maxvalue=float('-inf')

for i in range(len(walls)):
    for j in range(i+1,len(walls)):
        n=min(walls[i][1],walls[j][1])*(walls[j][0]-walls[i][0])
        if n>maxvalue:
            maxvalue=n

print(maxvalue)
'''

# 문제 3

'''
number=[7,3,4,1,2,5,6]
n=len(number)+1
ans=[]

number.sort()
a=list(number)

number.sort(reverse=True)
b=number

ans+=((a[:(n//2)-1]))
ans+=((b[:(n//2)]))

print(ans)
'''

# 문제 4
'''

number1='2433'
number2='662244'

n1=list(map(int,list(number1)))
n2=list(map(int,list(number2)))

n1.sort(reverse=True)
n2.sort(reverse=True)

cnt=0

for i in range(len(n1)):
    if i!=len(n1)-1 and n1[i]!=n1[i+1]:
        cnt+=1
        print("{}{}".format(n1[i],cnt),end='')
        cnt=0
    elif i==len(n1)-1:
        cnt+=1
        print("{}{}".format(n1[i],cnt),end='')
        cnt=0
    else:
        cnt+=1


print()

for i in range(len(n2)):
    if i!=len(n2)-1 and n2[i]!=n2[i+1]:
        cnt+=1
        print("{}{}".format(n2[i],cnt),end='')
        cnt=0
    elif i==len(n2)-1:
        cnt+=1
        print("{}{}".format(n2[i],cnt),end='')
        cnt=0
    else:
        cnt+=1
'''

# 문제 5

'''
e1=[1,4,3]
a1=[1,3]
e2=[1,1,1]
a2=[1,2,3,4]

e1.sort()
a1.sort()
e2.sort()
a2.sort()

cnt=0

i=0
j=0

while i<min(len(e1),len(a1)):
    if e1[j]<=a1[i]:
        cnt+=1
        j+=1
    i+=1

print(cnt)



cnt=0

i=0
j=0

while i<min(len(e2),len(a2)):
    if e2[j]<=a2[i]:
        cnt+=1
        j+=1
    i+=1

print(cnt)
'''

# 문제 6

s1=int(input())
s2=int(input())
p=int(input())
q=int(input())

s1=int(str(s1),p)
s2=int(str(s2),p)

