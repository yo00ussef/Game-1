print("What is the number of players?")
x=int(input())
if (x>2 or x==0):
    print("error number of players, there must not be more than two players,please enter the number of players correctly ")
    x=int(input())
if (x==2):
    player1=x-1
    player2=x
sum1=0
while(x==2):    
   print("player1 please enter your number :-")
   i=int(input())
   if(0<i<11):
       
       sum1=sum1+i

   else :
       print("your range is from 1 to 10 please enter your number correctly")
       i=int(input())
       sum1=sum1+i

   if(sum1+i==100):
       print("Player1 wins")
       break
   print("player2 please enter your number :-")
   y=int(input())
   if(0<y<11):
       
       sum1=sum1+y
   else :
       print("your range is from 1 to 10 please enter your number correctly")
       y=int(input())
       sum1=sum1+y
   if (sum1+y==100):
        print("Player2 wins")
        break
