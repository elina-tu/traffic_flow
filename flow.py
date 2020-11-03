import numpy as np
from numpy.random import default_rng
import flow_functions as ff

road_length = 10 #number of cells
density = 0.4 #num_cars/num_cells
num_cars = int(density*road_length) #number of cacrs
v_max = 5 #maximum velocity
time = 10

#craete an empty road
road = np.empty(road_length)
road[:] = np.NaN

#populate the road
rng = default_rng()
position = rng.choice(road_length, size=num_cars, replace=False)
position = np.sort(position)
velocity = np.random.random_integers(0, v_max, size=num_cars)
#test data
#position = np.array([1, 4])
#velocity = np.array([2, 1])

road[np.array(position)] = velocity

print('road: {}'.format(road))

for i in range(time):
    velocity = ff.speed_update(position, velocity, v_max, road_length)
    road, position = ff.position_update(road, position, velocity, road_length)

    print('road: {}'.format(road))
