from state import *
# import state
import numpy as np

def main():
    n=10
    starting=[0,0]
    ending=[9,9]
    Construct(n,starting,ending,True)
    i=0
    l=[]

    while(i<1000):
        if(i%100==0):
            Construct(n,starting,ending,False)
        l.append(SARSA(starting,ending,n,epsilon=0.1,alpha=1))
        i+=1
    with open("result.txt", "a") as myfile:
        myfile.write(str(l)+ '\n')
    print(l)


# implements the value_iteration method
def Construct(n,starting,ending,bool):
    L=[x for x in range(n)]
    for i in range(n):
        for j in range(n):
            reward=[]
            for k in range(4):
                reward.append(np.random.normal(-10,1.5))
            if(bool):
                Q=[0,0,0,0]
                Q2=[0,0,0,0]
                s=state(Q,Q2,reward,i,j)
                state.Array_States[(i,j)]=s
            else:
                state.Array_States[(i, j)].reward=reward


def SARSA(statrting,ending,n,epsilon,alpha):
    s1=state.Array_States[(statrting[0],statrting[1])]
    SUM_REWARD=0
    step=0
    a1 = policy(s1.Q, epsilon)
    while([s1.i,s1.j]!=ending):
        step+=1
        s2=state.Array_States[s1.state_transition(a1,s1.i,s1.j,n)]
        SUM_REWARD+=s1.reward[a1]
        a2 = policy(s2.Q, epsilon)
        s1.Q[a1]=s1.Q[a1]+alpha*(s1.reward[a1]+s2.Q[a2]-s1.Q[a1])
        s1=s2
        a1=a2
    print(step)
    return  SUM_REWARD


def Expected_SARSA(statrting,ending,n,epsilon,alpha):
    s1=state.Array_States[(statrting[0],statrting[1])]
    SUM_REWARD=0
    step=0
    a1 = policy(s1.Q, epsilon)
    while([s1.i,s1.j]!=ending):
        step+=1
        s2=state.Array_States[s1.state_transition(a1,s1.i,s1.j,n)]
        SUM_REWARD+=s1.reward[a1]
        a2 = policy(s2.Q, epsilon)
        Expected_Sum=0
        for i in range(4):
            if(i==a2):
                Expected_Sum+=(1-epsilon+epsilon/4)*s2.Q[a2]
            else:
                Expected_Sum += (epsilon) * s2.Q[i]
        s1.Q[a1]=s1.Q[a1]+alpha*(s1.reward[a1]+Expected_Sum-s1.Q[a1])
        s1=s2
        a1=a2
    print(step)
    return  SUM_REWARD

def Q_Learn(statrting,ending,n,epsilon,alpha):
    s1=state.Array_States[(statrting[0],statrting[1])]
    SUM_REWARD=0
    step=0
    a1 = policy(s1.Q, epsilon)
    while([s1.i,s1.j]!=ending):
        step+=1
        s2=state.Array_States[s1.state_transition(a1,s1.i,s1.j,n)]
        SUM_REWARD+=s1.reward[a1]
        a2 = policy(s2.Q, epsilon)
        s1.Q[a1]=s1.Q[a1]+alpha*(s1.reward[a1]+s2.Q[Max_index_List(s2.Q)]-s1.Q[a1])
        s1=s2
        a1=a2
    print(step)
    return  SUM_REWARD

def Double_SARSA(statrting,ending,n,epsilon,alpha):
    s1=state.Array_States[(statrting[0],statrting[1])]
    SUM_REWARD=0
    step=0
    a1 = policy(s1.Q, epsilon)
    while([s1.i,s1.j]!=ending):
        step+=1
        s2=state.Array_States[s1.state_transition(a1,s1.i,s1.j,n)]
        SUM_REWARD+=s1.reward[a1]
        a2 = policy(s2.Q, epsilon)
        i = np.random.uniform(0, 1)
        bool=False
        if(i<0.5):
            bool=True
        if(bool):
            s1.Q[a1]=s1.Q[a1]+alpha*(s1.reward[a1]+s2.Q2[a2]-s1.Q[a1])
        else:
            s1.Q2[a1]=s1.Q2[a1]+alpha*(s1.reward[a1]+s2.Q[a2]-s1.Q2[a1])
        s1=s2
        a1=a2
    print(step)
    return  SUM_REWARD


def policy(Q,epsilon):
    i=np.random.uniform(0,1)
    bool = False
    if (i <= epsilon):
        bool = True
    j = 0
    if (bool == False):
        j = Max_index_List(Q)
    else:
        j = np.random.randint(0, len(Q))
    if(j<0):

        print(j)
    return j

def policy_DoubleQ(Q,Q2,epsilon):
    i=np.random.uniform(0,1)
    j=np.random.uniform(0,1)
    bool2=False
    if(j<0.5):
        bool2=True
    bool = False
    if (i <= epsilon):
        bool = True
    j = 0
    if (bool == False):
        if(bool2):
            j = Max_index_List(Q)
        else:
            j = Max_index_List(Q2)
    else:
        j = np.random.randint(0, len(Q))
    if(j<0):
        print(j)
    return j


def Max_index_List(Q):
    max=-(10**(10000))**100
    i=-1
    j=0
    for q in Q:
        if(q>max):
            max=q
            i=j
        j+=1
    return i




def print_maze(k,n):
    print(k)
    for i in range(n):
        print("||", end=" ")
        for j in range(n):
            print(str(state.Array_States[(i, j)].value) + "," + str(state.Array_States[(i, j)].optimal_action),
                  end=" || ")
        print("")
        print("-------------------------")



if __name__ == '__main__':
    main()


