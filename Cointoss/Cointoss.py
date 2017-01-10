def Cointoss():
    side=""
    headcount=0
    tailcount=0
    for i in range(0,5000):
        import random
        x=random.random()
        if x<0.5:
            side="tails"
            tailcount=tailcount+1
        elif x>= 0.5:
            side="heads"
            headcount=headcount+1
        print "Attempt #{}:Throwing a coin... It's {}! Got {} heads and {} tails so far".format(i+1,side, headcount,tailcount)
    print "Good job. Game over"
Cointoss()
