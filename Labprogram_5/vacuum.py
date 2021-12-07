import random
#intially completely dirty:
room=[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]

def percieve():
    per=[]
    for i in range(4):
        t=[]
        for j in range(4):
            t.append(random.randint(0,1))
        per.append(t)
    return per

def clean(proom):
    count=0
    for i in range(4):
        for j in range(4):
            if(proom[i][j]==1):
                proom[i][j]=0
                print(proom)
                count=count+1
    return count

def main():
    proom=percieve()
    print("The dirt detected:")
    print(proom)
    count=clean(proom)
    perf=count/16*100
    print("Efficiency: ",perf,"%")
main()



