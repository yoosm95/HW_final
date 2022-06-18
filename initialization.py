import random
from setting import *

init = float("inf")

iv_pos = [] # particle invidisual position
iv_vel = [] # particle invidisual velocity
iv_ft = []
lb_pos = [] # local best particle position
lb_ft = []
for i in range(p_size):
	iv_ft.append(init)
	lb_pos.append(init)
	lb_ft.append(init) #fitness local best particle position
#gb_pos = []  #global best particle position
gb_ft = init #fitness global best particle position

swarm_pos = []
swarm_vel = []
for i in range(p_size):
        iv_pos = []
        iv_vel = []
        for j in range(dv):
                iv_pos.append(random.uniform(bounds[j][0], bounds[j][1]))
                iv_vel.append(random.uniform(-1,1))
        swarm_pos.append(iv_pos)
        swarm_vel.append(iv_vel)
#print(swarm_pos[1])
#print(swarm_vel)
#print(lb_pos)
