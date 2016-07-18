'''
Created on Jun 16, 2016
 
@author: fil
'''
def fib():
    F = [1,1]
    user_input_x = int(input("Starting Index: "))
    user_input_y = int(input("Ending Index: "))
    if user_input_y == 1:
        F = [1]
    elif user_input_y < 1:
        print("Invalid Range")
        quit()
    elif user_input_x < 0:
        print("Invalid Range")
        quit()   
    elif user_input_x > user_input_y:
        print("Invalid Range")
        quit()
    elif user_input_x == user_input_y:
        print("Invalid Range")
        quit()
    else:
        for i in range(2,user_input_y):
            z = F[i-1]+F[i-2]
            F.append(z);
        #print(F)
       
        if user_input_x == 0:
            x1 = 1
        elif user_input_x == 1:
            x1 = 0
        else:
            x1 = F[user_input_x - 2]
       
        if user_input_x == 0:
            x2 = 0
        elif user_input_x == 1:
            x2 = 1
        else:
            x2 = F[user_input_x - 1]
       
        #print(x1, x2)
    x3 = x1+x2
    G = [x3,x3+x2]
    #print(G)
    #print(G)
    for i in range(2,user_input_y-user_input_x+1):
            w = G[i-1]+G[i-2]
            G.append(w);
    #print(G)
    print("Your Fibonacci Sequence is: ")
    print(G)
fib()