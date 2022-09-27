## RATIONAL AGENT: GESTURE 

gesture= ['Smile', 'Tired', 'Thirsty', 'Increase-Heart-Beat']

def make_agent(gesture):
    return[gesture]
agent_one_a = make_agent(gesture[1])

import random

def generate_random_gest(N):
    new_gest_random=[]
    for i in range(N):
        g1=random.choice(gesture)
        select_random_gesture=make_agent(g1)
        new_gest_random.append(select_random_gesture)
    return new_gest_random

random_gest_ans=generate_random_gest(1)
print("Agent gesture is ::")
print(random_gest_ans)

if random_gest_ans==[['Smile']]:
    print("Your agent is sitting and is relexing")

elif random_gest_ans==[['Tired']]:
    print("Your agent is standing")
        
elif random_gest_ans==[['Thirsty']]:
    print("Your agent is walking")

elif random_gest_ans==[['Increase-Heart-Beat']]:
    print("Your agent is running")
    
print('========================================')


## RATIONAL AGENT: Mood

mood= ['Happy', 'sad', 'Neutral']

def make_agent(mood):
    return[mood]
agent_one_a = make_agent(mood[1])

import random

def generate_random_mud(N):
    new_mud_random=[]
    for i in range(N):
        g1=random.choice(mood)
        select_random_mud=make_agent(g1)
        new_mud_random.append(select_random_mud)
    return new_mud_random

random_mud_ans=generate_random_mud(1)
print("Agent mood is ::")
print(random_mud_ans)

if random_mud_ans==[['Happy']]:
    print("Your agent is sitting and is relexing")

elif random_mud_ans==[['sad']]:
    print("Your agent is standing")
        
elif random_mud_ans==[['Neutral']]:
    print("Your agent is walking")

