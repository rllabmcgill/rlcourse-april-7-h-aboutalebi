# actions: 0 for left, 1 for right, 2 for up, 3 for down

class state:
    Array_States={}
    def __init__(self,Q,Q2,reward,i,j):
        self.Q=Q
        self.Q2=Q2
        self.reward=reward
        self.i=i
        self.j=j
        self.optimal_action=0

# implements state transition function
    def state_transition(self,action,i,j,n):
        if (action==0):
            if(j==0):
                return (i,j)
            if(j!=0):
                return (i,j-1)
        if (action==1):
            if(j==n-1):
                return (i,j)
            if(j!=n-1):
                return (i,j+1)
        if (action==2):
            if(i==0):
                return (i,j)
            if(i!=0):
                return (i-1,j)
        if (action==3):
            if(i==n-1):
                return (i,j)
            if(i!=n-1):
                return (i+1,j)