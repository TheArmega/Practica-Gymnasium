#!/usr/bin/env python

import gymnasium as gym
import gymnasium_csv

import numpy as np
import time

"""
# Coordinate Systems for `.csv` and `print(numpy)`

X points down (rows); Y points right (columns); Z would point outwards.

*--> Y (columns)
|
v
X (rows)
"""
UP = 0
UP_RIGHT = 1
RIGHT = 2
DOWN_RIGHT = 3
DOWN = 4
DOWN_LEFT = 5
LEFT = 6
UP_LEFT = 7

SIM_PERIOD_MS = 500.0

env = gym.make('gymnasium_csv-v0',
                render_mode='human',  # "human", "text", None
                inFileStr='../assets/map2.csv',
                initX=1,
                initY=1,
                goalX=8,
                goalY=16)
observation, info = env.reset()
print("observation: "+str(observation)+", info: "+str(info))
env.render()
time.sleep(0.5)

moves = [DOWN_RIGHT, RIGHT, DOWN_RIGHT, RIGHT, DOWN_RIGHT, RIGHT, DOWN_RIGHT, RIGHT, DOWN_RIGHT, RIGHT, DOWN_RIGHT, RIGHT, DOWN_RIGHT, RIGHT, RIGHT]

for i in moves:
        observation, reward, terminated, truncated, info = env.step(i)
        env.render()
        print("observation: " + str(observation)+", reward: " + str(reward) + ", terminated: " +
                str(terminated) + ", truncated: " + str(truncated) + ", info: " + str(info))
        time.sleep(SIM_PERIOD_MS/1000.0)
