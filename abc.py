def dfs(start):
    global visit
    s=[start]
    d=[]

    if start not in visit:
        while s:
            x=s.pop()
            visit.append(x)
            d.append(x)

            for i in g[x]:
                if i not in visit:
                    s.append(i)

        return d
    


k,n=map(int,input().split())
g={}
visit=[]

for i in range(1,k+1):
    g[i]=[i]

for i in range(n):
    a,b=map(int,input().split())
    g[a].append(b)



dfsvalue=dfs(1)


reverse={}
for i in range(1,k+1):
    reverse[i]=[]

for i in g:
    for j in g[i]:
        reverse[j].append(i)
g=reverse



ans=[]
visit=[]
for i in dfsvalue:
    scc=dfs(i)
    
    if scc!=None:
        scc.sort()
        ans.append(scc)


ans.sort()

print(len(ans))

for i in range(len(ans)):
    for j in range(len(ans[i])):
        print(ans[i][j],end=' ')
    print(-1)