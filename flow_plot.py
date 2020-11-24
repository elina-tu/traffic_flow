import numpy as np
from numpy.random import default_rng
import flow_functions as ff
import matplotlib.pyplot as plt

road_length = 100 #number of cells
in_density = 0.05 #num_cars/num_cells
rand_slow_chance = 0.2 #chance of the car randomly slowing down
v_max = 5 #maximum velocity
road = 0
time = 100

step = 0.1
runs = 50
final_val = 1
k = 0
density_arr = np.concatenate((np.arange(0.01, 0.2, 0.02), np.arange(0.25, 1, 0.05)))
#density_arr = np.arange(in_density, final_val, step)

#flow_arr = np.empty(int((np.floor((final_val - in_density)/step) + 1), ))
flow_arr = np.empty_like(density_arr)
for density in density_arr:
    flow_avr = np.zeros((runs, ))
    num_cars = int(density*road_length) #number of cacrs

    for j in range(runs): 
        car_count = 0
        #populate the road
        rng = default_rng()
        position = rng.choice(road_length, size=num_cars, replace=False)
        position = np.sort(position)
        #velocity = np.random.random_integers(0, v_max, size=num_cars)
        velocity = np.zeros(num_cars)

        #setting initial conditions
        for i in range(5*road_length):
            velocity = ff.speed_update(position, velocity, v_max, road_length,\
                                                          rand_slow_chance, num_cars)
            position = ff.position_update(road, position, velocity, road_length)

        #main loop moving cars
        for i in range(time):

            velocity = ff.speed_update(position, velocity, v_max, road_length,\
                                                           rand_slow_chance, num_cars)
            car_count = ff.counting_cars(position, velocity, road_length, car_count)
            position = ff.position_update(road, position, velocity, road_length)

        #print(car_count)
        flow_avr[j] = ff.measure_flow(time, car_count)

    #print(flow_avr)
    flow_arr[k] = np.mean(flow_avr)
    k += 1

plt.plot(density_arr, flow_arr, 'rx')
plt.xlabel('Density')
plt.ylabel('Flow')
plt.show()
