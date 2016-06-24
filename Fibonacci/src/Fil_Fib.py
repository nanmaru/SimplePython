'''
Created on Jun 23, 2016

@author: Fil Gibarac
'''
def fib(x):
   
    F = [1,1]
    for i in range(2,x+1):
        y = F[i-1] +F[i-2]
        F.append(y);
    print(F);
           
print(fib(7))