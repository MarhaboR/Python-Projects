action = ['Smile', 'Frown', 'Nod', 'Blink']

gesture= ['Positive', 'Negative', 'Unsure']


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

mood= ['Happy', 'sad', 'Neutral']

def make_agent(mood):
    return[mood]
agent_one_a = make_agent(mood[1])

import random

def generate_random_mud(M):
    new_mud_random=[]
    for i in range(M):
        g1=random.choice(mood)
        select_random_mud=make_agent(g1)
        new_mud_random.append(select_random_mud)
    return new_mud_random

random_mud_ans=generate_random_mud(1)


if random_mud_ans==[['Happy']] and random_gest_ans==[['Positive']]:
    print('If ',random_mud_ans,'and', random_gest_ans,",",action[0])
    
elif random_mud_ans==[['Happy']] and random_gest_ans==[['Negative']]:
    print('If ',random_mud_ans,'and', random_gest_ans,",",action[0])
    
elif random_mud_ans==[['Happy']] and random_gest_ans==[['Unsure']]:
    print('If ',random_mud_ans,'and', random_gest_ans,",",action[2])

elif random_mud_ans==[['sad']] and random_gest_ans==[['Negative']]:
    print('If ',random_mud_ans,'and', random_gest_ans,",",action[1])
        
        
elif random_mud_ans==[['sad']] and random_gest_ans==[['Positive']]:
    print('If ',random_mud_ans,'and', random_gest_ans,",",action[1])
        
elif random_mud_ans==[['sad']] and random_gest_ans==[['Unsure']]:
    print('If ',random_mud_ans,'and', random_gest_ans,",",action[1])
        
        
elif random_mud_ans==[['Neutral']]and random_gest_ans==[['Positive']]:
    print('If ',random_mud_ans,'and', random_gest_ans,",",action[2])
    
    
elif random_mud_ans==[['Neutral']]and random_gest_ans==[['Negative']]:
    print('If ',random_mud_ans,'and', random_gest_ans,",",action[2])

elif random_mud_ans==[['Neutral']]and random_gest_ans==[['Unsure']]:
    print('If ',random_mud_ans,'and', random_gest_ans,",",action[3])