# 문제 1
'''
def bfs(y,x):
    dy=[1,-1,0,0]
    dx=[0,0,1,-1]
    q=[(y,x)]
    
    while q:
        n=q.pop(0)
        for i in range(4):
            if n[0]+dy[i]<len(garden) and n[0]+dy[i]>=0 and n[1]+dx[i]<len(garden[1]) and n[1]+dx[i]>=0:
                
                if garden[n[0]+dy[i]][n[1]+dx[i]]==0 or garden[n[0]][n[1]]+1<garden[n[0]+dy[i]][n[1]+dx[i]]:
                    garden[n[0]+dy[i]][n[1]+dx[i]]=garden[n[0]][n[1]]+1
                    q.append((n[0]+dy[i],n[1]+dx[i]))

#garden=[[0,0,0],[0,1,0],[0,0,0]]
garden=[[1,1],[1,1]]

for i in range(len(garden)):
    for j in range(len(garden[i])):
        if garden[i][j]==1:
            bfs(i,j)

for i in garden:
    maxvalue=max(i)

print(maxvalue-1)
print(garden)

'''



# 문제 2
'''
def words(word):
    cnt=0
    sent=word[0]
    for i in range(1,len(word)):

        if len(sent)+len(word[i])+1<=10:
          sent+=(' '+word[i])  

        else:
            sent=word[i]
            cnt+=1
        print(sent)
            
    cnt+=1
    return cnt


word=["nice","happy","hello","world","hi"]

print(words(word))

'''

# 문제 3
# 숙제: 문제 3번 다른 알고리즘으로 풀기

'''
from itertools import *

a=[9,11,9,6,4,19]
c=list(combinations(a,4))

minvalue=float('inf')

for i in c:
    i=list(i)
    i.sort()
    
    minvalue=min(i[len(i)-1]-i[0],minvalue)

print(minvalue)
'''


# 문제 3(2)

'''
a=[9,11,9,6,4,19]

#[4,6,9,9,11,19]
k=4
a.sort()

minvalue=float('inf')
for i in range(len(a)-k+1):
    minvalue=min(minvalue,a[i+k-1]-a[i])

print(minvalue)

'''

# 문제 4

'''
n=6
t=3
k=3

card=[i for i in range(1,n+1)]
right=n
half=n//2
for i in range(t):
    a=card[half:right]
    b=card[:half]
    card=[]
    for j in range(len(a)):
        card.append(b[j])
        card.append(a[j])

print(card)
'''

# 문제 5

'''
board=[[0,0,0,0,0],[0,6,7,1,2],[0,3,5,3,9],[0,6,4,5,2],[0,7,3,2,6]]

for i in range(1,len(board)):
    for j in range(1,len(board[i])):
        board[i][j]=max(board[i][j]+board[i-1][j],board[i][j]+board[i][j-1])

print(board[len(board)-1][len(board)-1])
'''

# 문제 6

grid=[[1,4,16,1],[20,5,15,8],[6,13,36,14],[20,7,19,15]]

maxvalue=float('-inf')

for k in range(4):
    for i in range(4):
        for j in range(i+1,4):
            maxvalue=max(maxvalue,grid[i][k]+grid[j][k])


for k in range(4):
    for i in range(4):
        for j in range(i+1,4):
            maxvalue=max(maxvalue,grid[k][i]+grid[k][j])

print(maxvalue)