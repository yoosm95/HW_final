import numpy as np
import random
import os
from MOTA import MOTA

p_size = 20
max_iter = 50
dv = 4
weight = 0.9
c1 = 0.5
c2 = 0.5

bounds = [(1,20),(1,2000),(0.01,1),(0.1,0.5)]

def obj(x) :
	dir = 'car'
	os.system(f'python sort.py --seq_path={dir} '
			  f'--input_case={dir} --R={x[0]} --P={x[1]} --Q={x[2]} --iou_threshold={x[3]}')
	MOTA("./car/train", "mota_person.txt")
	mota = np.loadtxt("mota_person.txt")
	results = np.sum(mota) / len(mota)
	# results = mota
	return -results

