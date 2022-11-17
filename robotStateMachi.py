# https://github.com/pytransitions/transitions

from transitions import Machine, State
from robotClasses import *

wallyActivity = RobotActivity()

# The states

states = [
    'home',
    State(name='exploration', on_enter=['exploreWithTrajectory']),
    State(name='catch', on_enter=['openEffector']),
    State(name='throw', on_exit=['openEffector'])
    ]

#states=['home', 'exploration', 'catch', 'throw']

# And some transitions between states. 
transitions = [
    { 'trigger': 'start', 'source': 'home', 'dest': 'exploration' },
    { 'trigger': 'object_dectected', 'source': 'exploration', 'dest': 'catch' },
    { 'trigger': 'object_catched', 'source': 'catch', 'dest': 'throw' },
    { 'trigger': 'object_fallen', 'source': 'throw', 'dest': 'exploration' }
]
# Initialize
machine = Machine(wallyActivity, states=states, transitions=transitions, initial='home')





