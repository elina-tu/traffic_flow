import numpy as np
from numpy.random import default_rng
import flow_functions as ff
import matplotlib.pyplot as plt

road_length = 100 #number of cells
density = 0.2 #num_cars/num_cells
rand_slow_chance = 0.2 #chance of the car randomly slowing down
num_cars = int(density*road_length) #number of cacrs
v_max = 5 #maximum velocity
time = 20

#craete an empty road
road = np.empty(road_length)
road[:] = np.NaN

#populate the road
rng = default_rng()
position = rng.choice(road_length, size=num_cars, replace=False)
position = np.sort(position)
velocity = np.random.random_integers(0, v_max, size=num_cars)
#test data
#position = np.array([10])
#velocity = np.array([2])

#velocity of the car in corresponding position
road[np.array(position)] = velocity

#velocity array
velocity_arr = np.empty(num_cars*(time + 1))
velocity_arr[:num_cars] = velocity
#position array
position_arr = np.empty(num_cars*(time + 1))
position_arr[:num_cars] = position
#time array
time_arr = np.empty(num_cars*(time + 1))
time_arr[:num_cars] = np.zeros(num_cars)

#main loop moving cars
for i in range(time):

    velocity = ff.speed_update(position, velocity, v_max, road_length,\
                                                    rand_slow_chance, num_cars)
    road, position = ff.position_update(road, position, velocity, road_length)

    #storing values to plot
    velocity_arr[(i+1)*num_cars:(i+2)*num_cars] = velocity
    position_arr[(i+1)*num_cars:(i+2)*num_cars] = position
    time_arr[(i+1)*num_cars:(i+2)*num_cars] = (i+1)*np.ones(num_cars)

#plotting traffic
fig, ax = plt.subplots()

sc = plt.scatter(position_arr, time_arr, c=velocity_arr)

ax.set_ylim(time + 1, -1)
plt.xlabel('Position')
plt.ylabel('Time')
plt.title('Simulated traffic of low density')

plt.colorbar(sc)
plt.clim(0, v_max)

plt.show()
