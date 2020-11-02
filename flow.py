import numpy as np
from numpy.random import default_rng

road_lenght = 10 #number of cells
density = 0.5 #num_cars/num_cells
num_cars = int(density*road_lenght) #number of cacrs
v_max = 5 #maximum velocity

#craete an empty road
road = np.empty(road_lenght)
road[:] = np.NaN

#populate the road
rng = default_rng()
cars = rng.choice(road_lenght, size=num_cars, replace=False)
velocity = np.random.random_integers(0, v_max, size=num_cars)
road[np.array(cars)] = velocity
