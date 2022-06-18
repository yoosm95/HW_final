import numpy as np
import random
import time
from setting import *
from initialization import *
from matplotlib import pyplot as plt

def update_velocity(swarm_pos, swarm_vel, lb_pos, gb_pos, bounds):
	for i in range(dv):
		r1 = random.uniform(0,1)
		r2 = random.uniform(0,1)

		cognitive_vel = c1 * r1 * (lb_pos[i] - swarm_pos[i])
		social_vel = c2 * r2 * (gb_pos[i] - swarm_pos[i])
		swarm_vel[i] = weight * swarm_vel[i] + cognitive_vel + social_vel

		if abs(swarm_vel[i]) > 0.2 * bounds[i][1]:
			if swarm_vel[i] > 0:
				swarm_vel[i] = 0.2 * bounds[i][1]
			else:
				swarm_vel[i] = -0.2 * bounds[i][1]
	return swarm_vel

def update_position(swarm_pos, swarm_vel, bounds):
	new_swarm_pos = []
	r = random.uniform(0, 1)
	for i in range(dv):
		new_swarm_pos.append(swarm_pos[i] + swarm_vel[i])

		if new_swarm_pos[i] > bounds[i][1]:
			new_swarm_pos[i] = bounds[i][1] - r * swarm_vel[i]
		if new_swarm_pos[i] < bounds[i][0]:
			new_swarm_pos[i] = bounds[i][0] - r * swarm_vel[i]

	return new_swarm_pos

history = [] #optimum history
history_x = [] #particle history
history_y = [] #particle history
iteration = [] #for visualization

start_time = time.time()

for i in range(max_iter):
	print("iteration", i + 1)
	# Sharing information
	for j in range(p_size):
		iv_ft[j] = obj(swarm_pos[j])
		if iv_ft[j] < lb_ft[j]:
			lb_pos[j] = swarm_pos[j]
			lb_ft[j] = iv_ft[j]
		if iv_ft[j] < gb_ft:
			gb_pos = swarm_pos[j]
			gb_ft = iv_ft[j]


	# update velocity and position
	for k in range(p_size):
		swarm_vel[k] = update_velocity(swarm_pos[k], swarm_vel[k], lb_pos[k], gb_pos, bounds)
		swarm_pos[k] = update_position(swarm_pos[k], swarm_vel[k], bounds)

	history.append(gb_ft)
	it = i +1
	iteration.append(it)

# Results
print("optimal position:",gb_pos)
print("optimal solution:",gb_ft)
print("time cost :", time.time() - start_time)

# Visualization - 1
plt.plot(iteration, history)
plt.title("Change of optimum")
plt.xlabel("iteration")
plt.ylabel("optimum")
plt.show()


#particle_change(-1,history_x,history_y)
