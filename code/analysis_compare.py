import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import sys

k5_file_name = sys.argv[1]
k11_file_name = sys.argv[2]

epoch = 0
rewards_epoch = []
step_episodes = [] 
last_step = 10000
k5_avg_epoch_rewards = []
k11_avg_epoch_rewards = []
step_epoch = 10000

def compute_rewards():
    global epoch, step_epoch, rewards_epoch, step_episodes, last_step, k5_avg_epoch_rewards, k11_avg_epoch_rewards
    if epoch == 0:
        epoch += 1
        return 
    step_episodes.append(last_step)
    total = 0
    for i in range(len(rewards_epoch)):
        total += rewards_epoch[i] * step_episodes[i]
    avg_reward = total/ step_epoch
    rewards_epoch = []
    step_episodes = []
    if k5:
        k5_avg_epoch_rewards.append(avg_reward)
    else:
        k11_avg_epoch_rewards.append(avg_reward)
    print 'epoch ', epoch, ' avg reward epoch ', avg_reward 
    epoch += 1
    last_step = 10000

k5 = True
with open(k5_file_name, 'rb') as in_file:
    lines = in_file.readlines()

for line in lines:
    if 'epoch' in line:
        line_split = line.split()
        current_epoch = int(line_split[2])
        if current_epoch > epoch:
            compute_rewards()
        else:
            step = int(line_split[-1])
            step_episodes.append(last_step - step)
            last_step = step
    if 'reward' in line:
        rewards_epoch.append(float(line.split()[-1]))

k5_epoch = epoch
k5 = False
print 'k=11 =========================='
epoch = 0
with open(k11_file_name, 'rb') as in_file:
    lines = in_file.readlines()

for line in lines:
    if 'epoch' in line:
        line_split = line.split()
        current_epoch = int(line_split[2])
        if current_epoch > epoch:
            compute_rewards()
        else:
            step = int(line_split[-1])
            step_episodes.append(last_step - step)
            last_step = step
    if 'reward' in line:
        rewards_epoch.append(float(line.split()[-1]))


import ipdb; ipdb.set_trace()
plt.plot(range(1, k5_epoch), k5_avg_epoch_rewards)
plt.plot(range(1, epoch), k11_avg_epoch_rewards)
plt.ylabel('average reward per 10,000 steps')
plt.xlabel('epoch (10,000 steps) number')
plt.savefig('space_k5_k11_comparison_plot.jpg')



