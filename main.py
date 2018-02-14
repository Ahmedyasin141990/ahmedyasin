print("welcome to our game")
while("true"):
  c=int(input("please enter your coins num:"))
  while(c<=0):
     print("coins should not be less than or equal zero")
     c=int(input("please enter your coins num:"))
     if(c<=0):
      print("coins should not be less than or equal zero")
     break
  if(c>0):
    p1=int(input("Take coins you want player1:"))
    while(p1>=c or p1<=0):
      
      print("you should choose coins number less than coins number and not equal zero")
      p1=int(input("Take coins you want player1:"))
      
    if (p1<c and p1>0):
        c=c-p1
       
    
    print("coins remain:",c) 
    while("true"):
     p2=int(input("Take coins you want player2:"))
     while (p2>2*p1 or p2<=0 or p2>c):
         print("you should take coins number less than or equal double player1 coins and not equalzero")
         p2=int(input("Take coins you want player2:"))
         
     if (p2<=2*p1 and p2>0 and p2<=c):
          c=c-p2
      
     
     
     print("coins remain:",c) 
     if (c==0):
           print ("player2 wins")
           print ("-"*80)
           break
           c=c-p2
     if (c>0):
           p1=int(input("Take coins you want player1:"))
           while(p1>2*p2 or p1<=0):
             print ("you should take coins number less than double player2 coins and not equal zero")
             p1=int(input("Take coins you want player1:"))
             
           if (p1<=2*p2 and p1>0 and p1<=c):
               c=c-p1
           
           print("coins remain:",c) 
           if(c==0):
             print("player1 wins")
             print ("-"*80)
             break
             

             
            
            
           
     
