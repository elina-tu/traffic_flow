import numpy as np

def position_update(road, position, velocity, road_length):
    road[:] = np.NaN
    position = (position + velocity)%road_length
    road[np.array(position)] = velocity
    return road, position

def speed_update(position, velocity, v_max, road_length):
    #how far many spaces to the next car
    space_next_car = np.diff(position, append=position[0])%road_length
    for i in range(len(position)):
        if (velocity[i] + 1 < space_next_car[i]) & (velocity[i] < v_max):
            velocity[i] += 1
        elif space_next_car[i] <= velocity[i]:
            velocity[i] = space_next_car[i] - 1
    return velocity
