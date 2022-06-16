import random as rand
from itertools import combinations
sRank={'C':0,'D':1,'H':2,'S':3}
vRank={'A':14,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13}
tToRank={'RoyalFlush':10,'StraightFlush':9,'Four':8,'FullHouse':7,'Flush':6,'Straight':5,'Three':4,'TwoPair':3,'OnePair':2,'HighCard':1}
comb65=list(combinations("012345",5))
comb75=list(combinations("0123456",5))
def cardRank(card):
    s=card[0]
    v=card[1:]
    rank=vRank[v]
    return rank

def cardSort(cards):
    n=len(cards)
    for i in range(n-1):
        for j in range(n-i-1):
            if(cardRank(cards[j])>cardRank(cards[j+1])):
                t=cards[j]
                cards[j]=cards[j+1]
                cards[j+1]=t
    return cards

def typeToRank(s):
    return tToRank[s]

def cardsType(cards):
    cards=cardSort(cards)
    if(isRoyalFlush(cards)):
        return 'RoyalFlush'
    elif (isStraightFlush(cards)):
        return 'StraightFlush'
    elif (isFour(cards)):
        return 'Four'
    elif (isFullHouse(cards)):
        return 'FullHouse'
    elif (isFlush(cards)):
        return 'Flush'
    elif (isStraight(cards)):
        return 'Straight'
    elif (isThree(cards)):
        return 'Three'
    elif (isTwoPair(cards)):
        return 'TwoPair'
    elif (isOnePair(cards)):
        return 'OnePair'
    elif (isHighCard(cards)):
        return 'HighCard'


def isRoyalFlush(cards):
    a=[]
    a.append(['CT','CJ','CQ','CK','CA'])
    a.append(['DT','DJ','DQ','DK','DA'])
    a.append(['HT','HJ','HQ','HK','HA'])
    a.append(['ST','SJ','SQ','SK','SA'])
    for i in range(4):
        if(cards == a[i]):
            return True
    return False
        
def isStraightFlush(cards):
    suit=cards[0][0]
    for c in cards:
        if(c[0] != suit):
            return False        
    x=[]
    for c in cards:
        x.append(cardRank(c))
    if(x[-1]-x[0]!=4):
        return False
    return True

def isFour(cards):
    x=[0 for i in range(15)]
    for c in cards:
        x[vRank[c[1:]]]+=1
    for a in x:
        if a ==4:
            return True
    return False

def isFullHouse(cards):
    x=[0 for i in range(15)]
    for c in cards:
        x[vRank[c[1:]]]+=1
    c2=0
    c3=0
    for a in x:
        if a ==2:
            c2+=1
        elif a == 3:
            c3+=1
    if(c2==1 and c3 ==1):
        return True
    return False
def isFlush(cards):
    suit=cards[0][0]
    for c in cards:
        if(c[0] != suit):
            return False        
    return True
def isStraight(cards):   
    x=[0 for i in range(15)]
    for c in cards:
        x[vRank[c[1:]]]+=1
    for i in range(2,11):
        flag=True
        for j in range(5):
            if(x[j+i]!=1):
                flag=False
                break
        if(flag==True):
            return True
    return False   
def isThree(cards):
    x=[0 for i in range(15)]
    for c in cards:
        x[vRank[c[1:]]]+=1
    for a in x:
        if a == 3:
            return True
    return False  
def isTwoPair(cards):
    x=[0 for i in range(15)]
    for c in cards:
        x[vRank[c[1:]]]+=1
    t2=0
    t1=0
    for a in x:
        if(a==2):
            t2+=1
        elif(a==1):
            t1+=1
    if(t2==2 and t1 ==1):
        return True
    return False   
def isOnePair(cards):
    x=[0 for i in range(15)]
    for c in cards:
        x[vRank[c[1:]]]+=1
    t2=0
    t1=0
    for a in x:
        if(a==2):
            t2+=1
        elif(a==1):
            t1+=1
    if(t2==1 and t1 ==3):
        return True
    return False   
def isHighCard(cards):
    return True
def isPair(cards):
    if(cards[0][1:]==cards[1][1:]):
        return True
    return False
def preFlopLevel(h):
    h=cardSort(h)
    v0=vRank[h[0][1:]]
    v1=vRank[h[1][1:]]
    if(isPair(h)):   
        if(v1>=10):
            return 10
        elif (v1>=6):
            return 8
        else:
            return 6
    if(v1>=10 and v0 >=10):
        return 9
    elif(v1>=6 and v0 >=6):
        return 4
    else:
        if(v1==14):
            return 7
        elif (v1>=10):
            return 5
        else:
            return 1
def findBiggest(cards):
    if(len(cards)==5):
        return tToRank[cardsType(cards)]
    elif(len(cards)==6):
        x=-1
        for tp in comb65:
            c=[]
            for t in tp:
                c.append(cards[int(t)])
            x=max(x,tToRank[cardsType(c)])   
        return x  
    elif(len(cards)==7):
        x=-1
        for tp in comb65:
            c=[]
            for t in tp:
                c.append(cards[int(t)])
            x=max(x,tToRank[cardsType(c)])
        return x
def preFlop(actions, hand, state):
    v = 0
    cardLevel=0
    level = preFlopLevel(hand)
    if(level>=6):
        amount = actions[2]['amount']
        v = min((amount['min'] +50),amount['max'] )
        return 'raise',v
    else:
        amount = actions[1]['amount']
        if(level==1):
            if(amount>50):
                return 'fold',0
            return 'call',amount
        else:
            if(amount>100):
                return 'fold',0
            return 'call',amount

def theFlop(actions, hand, state):
    cards=cardSort(state['community_card']+hand)
    ct=findBiggest(cards)
    if(ct>=7):
        amount = actions[2]['amount']
        v = max(amount["min"],int(amount["max"]/3))
        return 'raise',v
    if(ct>=4):
        amount = actions[2]['amount']
        v = max(amount["min"],int(amount["max"]/5))
        return 'raise',v
    if(ct==3):
        amount = actions[1]['amount']
        if(amount>=300):
            return 'fold',0
        if(amount>=100):
            rd=rand.randrange(0,100)
            if(rd>10):
                return 'call',amount 
            else:
                return 'fold',0
        rd=rand.randrange(0,100)
        if(rd>20):
            return 'raise',actions[2]['amount']['min']
        return 'call',amount 
    if(ct==2):
        amount = actions[1]['amount']
        if(amount>=150):
            return 'fold',0
        if(amount>=50):
            rd=rand.randrange(0,100)
            if(rd>30):
                return 'call',amount 
            else:
                return 'fold',0
        rd=rand.randrange(0,100)
        if(rd>40):
            return 'raise',actions[2]['amount']['min']
        return 'call',amount 
    else:
        amount = actions[1]['amount']
        if(amount>50):
            return 'fold',0
        rd=rand.randrange(0,100)
        if(rd>50):
            return 'raise',actions[2]['amount']['min']
        return 'call',amount

def theTurn(actions, hand, state):
    cards=cardSort(state['community_card']+hand)
    ct=findBiggest(cards)
    if(ct>=7):
        amount = actions[2]['amount']
        v = max(amount["min"],int(amount["max"]/3))
        return 'raise',v
    if(ct>=4):
        amount = actions[2]['amount']
        v = max(amount["min"],int(amount["max"]/5))
        return 'raise',v
    if(ct==3):
        amount = actions[1]['amount']
        if(amount>=300):
            return 'fold',0
        if(amount>=100):
            rd=rand.randrange(0,100)
            if(rd>10):
                return 'call',amount 
            else:
                return 'fold',0
        rd=rand.randrange(0,100)
        if(rd>20):
            return 'raise',actions[2]['amount']['min']
        return 'call',amount 
    if(ct==2):
        amount = actions[1]['amount']
        if(amount>=150):
            return 'fold',0
        if(amount>=50):
            rd=rand.randrange(0,100)
            if(rd>30):
                return 'call',amount 
            else:
                return 'fold',0
        rd=rand.randrange(0,100)
        if(rd>40):
            return 'raise',actions[2]['amount']['min']
        return 'call',amount 
    else:
        amount = actions[1]['amount']
        if(amount>50):
            return 'fold',0
        rd=rand.randrange(0,100)
        if(rd>50):
            return 'raise',actions[2]['amount']['min']
        return 'call',amount
def theRiver(actions, hand, state):
    cards=cardSort(state['community_card']+hand)
    ct=findBiggest(cards)
    if(ct>=7):
        amount = actions[2]['amount']
        v = max(amount["min"],int(amount["max"]/3))
        return 'raise',v
    if(ct>=4):
        amount = actions[2]['amount']
        v = max(amount["min"],int(amount["max"]/5))
        return 'raise',v
    if(ct==3):
        amount = actions[1]['amount']
        if(amount>=300):
            return 'fold',0
        if(amount>=100):
            rd=rand.randrange(0,100)
            if(rd>40):
                return 'call',amount 
            else:
                return 'fold',0
        return 'call',amount 
    if(ct==2):
        amount = actions[1]['amount']
        if(amount>=150):
            return 'fold',0
        if(amount>=50):
            rd=rand.randrange(0,100)
            if(rd>60):
                return 'call',amount 
            else:
                return 'fold',0
        return 'call',amount 
    else:
        amount = actions[1]['amount']
        if(amount>50):
            return 'fold',0
        return 'call',amount
