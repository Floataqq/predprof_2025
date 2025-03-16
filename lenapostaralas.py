def lol(i,j,v,used,ans,ioi,op):

    if i==3:
        cnt=0
        for i in range(4):
            for j in range(3):
                for jkl in range(64):
                    cnt+=abs(v[ans[i][j]][jkl][-1]-v[ans[i][j+1]][jkl][0])
                    cnt+=abs(v[ans[j][i]][-1][jkl]-v[ans[j+1][i]][0][jkl])
        #print(op, cnt, ans, ioi)
        if cnt<op:
            for i in range(4):
                for j in range(4):
                    ioi[i][j]=ans[i][j]
            op=cnt

        return op
    i1=i
    j1=j+1
    if j1==3:
        j1=1
        i1+=1
    for o in range(16):
        if used[o]==0:
            used[o]=1
            ans[i][j]=o
            op=min(op,lol(i1,j1,v,used,ans,ioi,op))
            used[o]=0
    return op


def get(v):
    ans=[[-1 for _ in range(4)]for __ in range(4)]
    used=[0 for i in range(16)]
    for i in range(16):
        ok1=1
        ok2=1
        ok3=1
        ok4=1
        for j in range(64):
            if v[i][0][j]!=255:
                ok1=0
                break
        for j in range(64):
            if v[i][j][0]!=255:
                ok2=0
                break
        for j in range(64):
            if v[i][-1][j]!=255:
                ok3=0
                break
        for j in range(64):
            if v[i][j][-1]!=255:
                ok4=0
                break
        if ok1==1 and ok2==1:
            used[i]=1
            ans[0][0]=i
        elif ok1==1 and ok4==1:
            ans[0][3]=i
            used[i]=1
        elif ok2==1 and ok3==1:
            ans[3][0]=i
            used[i]=1
        elif ok3==1 and ok4==1:
            ans[3][3]=i
            used[i]=1
        elif ok1==1:
            if ans[0][1]==-1:
                ans[0][1]=i
                used[i]=1
            else :
                ans[0][2]=i
                used[i]=1
        elif ok2==1:
            if ans[1][0]==-1:
                ans[1][0]=i
                used[i]=1
            else:
                ans[2][0]=i
                used[i]=1
        elif ok3==1:
            if ans[3][1]==-1:
                ans[3][1]=i
                used[i]=1
            else:
                ans[3][2]=i
                used[i]=1
        elif ok4==1:
            if ans[1][3]==-1:
                ans[1][3]=i
                used[i]=1
            else:
                ans[2][3]=i
                used[i]=1
    cnt1=0
    for i in range(64):
        cnt1+=abs(v[ans[0][1]][i][0]-v[ans[0][0]][i][-1])
        cnt1 += abs(v[ans[0][2]][i][0] - v[ans[0][1]][i][-1])
        cnt1 += abs(v[ans[0][3]][i][0] - v[ans[0][2]][i][-1])
        cnt1 -= abs(v[ans[0][2]][i][0] - v[ans[0][0]][i][-1])
        cnt1 -= abs(v[ans[0][1]][i][0] - v[ans[0][2]][i][-1])
        cnt1 -= abs(v[ans[0][3]][i][0] - v[ans[0][1]][i][-1])
    if cnt1>0:
        ans[0][1],ans[0][2]=ans[0][2],ans[0][1]
    cnt1 = 0
    for i in range(64):
        cnt1 += abs(v[ans[-1][1]][i][0] - v[ans[-1][0]][i][-1])
        cnt1 += abs(v[ans[-1][2]][i][0] - v[ans[-1][1]][i][-1])
        cnt1 += abs(v[ans[-1][3]][i][0] - v[ans[-1][2]][i][-1])
        cnt1 -= abs(v[ans[-1][2]][i][0] - v[ans[-1][0]][i][-1])
        cnt1 -= abs(v[ans[-1][1]][i][0] - v[ans[-1][2]][i][-1])
        cnt1 -= abs(v[ans[-1][3]][i][0] - v[ans[-1][1]][i][-1])
    if cnt1 > 0:
        ans[-1][1], ans[-1][2] = ans[-1][2], ans[-1][1]
    cnt1=0
    for i in range(64):
        cnt1+=abs(v[ans[1][0]][0][i]-v[ans[0][0]][-1][i])
        cnt1 += abs(v[ans[2][0]][0][i] - v[ans[1][0]][-1][i])
        cnt1 += abs(v[ans[3][0]][0][i] - v[ans[2][0]][-1][i])
        cnt1 -= abs(v[ans[2][0]][0][i] - v[ans[0][0]][-1][i])
        cnt1 -= abs(v[ans[1][0]][0][i] - v[ans[2][0]][-1][i])
        cnt1 -= abs(v[ans[3][0]][0][i] - v[ans[1][0]][-1][i])
    if cnt1>0:
        ans[2][0],ans[1][0]=ans[1][0],ans[2][0]
    cnt1 = 0
    for i in range(64):
        cnt1 += abs(v[ans[1][-1]][0][i] - v[ans[0][-1]][-1][i])
        cnt1 += abs(v[ans[2][-1]][0][i] - v[ans[1][-1]][-1][i])
        cnt1 += abs(v[ans[3][-1]][0][i] - v[ans[2][-1]][-1][i])
        cnt1 -= abs(v[ans[2][-1]][0][i] - v[ans[0][-1]][-1][i])
        cnt1 -= abs(v[ans[1][-1]][0][i] - v[ans[2][-1]][-1][i])
        cnt1 -= abs(v[ans[3][-1]][0][i] - v[ans[1][-1]][-1][i])
    if cnt1 > 0:
        ans[2][-1], ans[1][-1] = ans[1][-1], ans[2][-1]
    goodans=[[0 for _ in range(4)] for __ in range(4)]
    cnt=1000000000000000
    lol(1,1,v,used,ans,goodans,cnt)
    return goodans

def p(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def getversh(x1,y1,x2,y2,a,b):
    ans=[]
    u=64
    while x1!=x2 or y1!=y2:
        x3=x1
        y3=y1
        for i in range(-u,u+1):
            for j in range(-u,u+1):
                if p(0,0,i,j)<=64:
                    x4=i+x1
                    y4=j+y1
                    if p(x4,y4,x2,y2)<=p(x3,y3,x2,y2):
                        x3=x4
                        y3=y4
        if x3!=x2 or y3!=y2:
            ans.append([[x3,y3],1])
        if u==64:
            u=128
        x1=x3
        y1=y3

    return ans
