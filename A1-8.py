print("Enter the number of coins :-")
coinnum=int(input())
a=2
b=0
while(a==2):
    print("player1 : your turn")
    x=int(input())
    if (x>0 and x<coinnum):
        b=b+x
    else:
        print("Wrong number of coins please enter the coins correctly")
        y=int(input())
        b=b+y
    if(b==coinnum):
        print("player1 wins")
        break
    print("player2 : your turn")
    n=int(input())
    if(n>0 and n<(2*x+1) and (n<coinnum) ):
        b=b+n
        
    else:
        print("Wrong number of coins please enter the coins correctly")
        p=int(input())
        b=coinnum-p
    if(b==coinnum):
        print("player2 wins")
        break     
