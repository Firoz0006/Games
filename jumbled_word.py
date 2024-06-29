

#jumbled word game
import random 

def choose():
    words=["COMPUTER","PROGRAM","COMPUTING","INTELLIGENCE","MEMORY","POWERPOINT","DATABASE","DATA",
           "ANALOGUE","DIGITAL","SIGNAL","BLOCK","CODER","DECODER","TRANSISTOR","SYSTEM","SCHEDULE",
           "ACCESS","CACHE","COOKIES","SIMULATION","UBUNTU","TELEVISION","MOBILE","SCIENCE","LOGIC",
           "ANALYTIC","MENTAL","ABILITY","TIME","NETWORK","GENERAL","PUBLIC","INTERNET","INTRANET",
           "WIRELESS","REMOTE","PROCESS","THREAD","THEORY","LEMMA","AXIOM","CABLE","OPERATING","WEB"
           ,"STORAGE"]
    pick=random.choice(words)
    return pick

def jumbled(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled


def thanks(p1n,p2n,p1,p2):
    print(p1n,"Your score is :",p1)
    print(p2n,"Your score is :",p2)
    print("Thank You for playing.")
    
def play():
    p1name=input("Player1 please, enter your name?--> ")
    p2name=input("Player2 please, enter your name?--> ")
    
    #points
    pp1=0
    pp2=0
    #turn variable
    turn=0
    while(1):
        picked_word=choose()
        qn=jumbled(picked_word)
        print("The jumble word is -")
        print(qn)
        if turn%2==0:
            print(p1name,"your turn please!")
            ans=input("what is in your mind?--> ")
            if(ans==picked_word):
                pp1=pp1+5
                print("Correct")
                print("Your score is :",pp1)
            else:
                print("Better luck next time")
                print("The correct answer is",picked_word)
            c=input("Press 1 to continue and 0 to quit--> ")
            c=int(c)
            if c==0:
                thanks(p1name,p2name,pp1,pp2)
                break
        else:
            print(p2name,"your turn please!")
            ans=input("what is in your mind?--> ")
            if ans==picked_word:
                pp2=pp2+5
                print("Correct")
                print("Your score is :",pp2)
            else:
                print("Better luck next time")
                print("The correct answer is",picked_word)
            c=input("Press 1 to continue and 0 to quit--> ")
            c=int(c)
            if c==0:
                thanks(p1name,p2name,pp1,pp2)
                break
        turn=turn+1    

play()