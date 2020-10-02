#problem solution
import math
T=int(input().strip())
A=[]
for t in range(T):
    A=input().split(" ")
    N=A[0]
    K=A[1]
    if(int(K)==1):
        print("NO")
    elif(math.sqrt(int(N))==int(K)):
        print("NO")
    elif((int(N)%(int(K)*int(K)))==0):
        print("NO")
    else:
        print("YES")
        
      
