import numpy as np

def position_update(road, cars, velocity, road_lenght):
    road[:] = np.NaN
    cars = (cars + velocity)%road_lenght
    road[np.array(cars)] = velocity
    return road, cars
