import json
from game.game import setup_config, start_poker
from agents.call_player import setup_ai as call_ai
from agents.random_player import setup_ai as random_ai
from agents.console_player import setup_ai as console_ai
from agents.agent import setup_ai as my_ai
from agents.a2 import setup_ai as my2_ai
from baseline0 import setup_ai as baseline0_ai
from baseline1 import setup_ai as baseline1_ai
from baseline2 import setup_ai as baseline2_ai
from baseline3 import setup_ai as baseline3_ai
import sys
gr=[]
xi=int(sys.argv[1])
t=int(sys.argv[2])
for i in range(t):
    config = setup_config(max_round=20, initial_stack=1000, small_blind_amount=5)
    if(xi==1):
        config.register_player(name="bot", algorithm= baseline1_ai())
    elif(xi==2):
        config.register_player(name="bot", algorithm= baseline2_ai())
    elif(xi==3):
        config.register_player(name="bot", algorithm= baseline3_ai())
    elif(xi==0):
        config.register_player(name="bot", algorithm= baseline0_ai())
    else:
        config.register_player(name="bot", algorithm= my_ai())
    config.register_player(name="me"+str(i), algorithm=my2_ai())

    ## Play in interactive mode if uncomment
    #config.register_player(name="me", algorithm=console_ai())
    game_result = start_poker(config, verbose=1)
    gr.append(game_result)
a=[0,0]
b=[]
cc=[0,0]
for g in gr: 
    print('===========================')
    p0=g['players'][0]
    p1=g['players'][1]
    if(p0['stack']>p1['stack']):
        a[0]+=1
        b.append(0)
    else:
        a[1]+=1
        b.append(1)
    print(p0)
    print(p1)
    cc[0]+=p0['stack']
    cc[1]+=p1['stack']
print(a[0],':',a[1])
print(b)
print(cc)
print('bot',xi)