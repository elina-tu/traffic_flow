import numpy as np

def position_update(road, position, velocity, road_length):
    '''function that updates position with accordance to velocity
    also creates road array that has values of velocities in corresponding position'''

    #road[:] = np.NaN
    #calculate new position and store it in the same array
    position = (position + velocity)%road_length
    #update road
    #road[np.array(position)] = velocity
    return position

def speed_update(position, velocity, v_max, road_length, rand_slow_chance, num_cars):
    '''function that updates velocities according to rules'''

    #how far is the next car
    space_next_car = np.diff(position, append=position[0])%road_length
    #generate uniform random intigers with probability for any given integer equal rand_slow_chance
    rand_slow = np.random.random_integers(0, int(1/rand_slow_chance), size=num_cars)
    #is there more than 1 car
    many_cars = num_cars > 1

    for i in range(num_cars):
        #speed up
        if (velocity[i] + 1 < space_next_car[i]) & (velocity[i] < v_max):
            velocity[i] += 1
        #slow down due to the next car
        elif (space_next_car[i] <= velocity[i]) & many_cars:
                velocity[i] = space_next_car[i] - 1
        #accelerating when there's only one car
        elif (not many_cars) & (velocity[i] < v_max):
            velocity[i] += 1
        #random slowing down
        if (velocity[i] > 0) & (rand_slow[i] == 0):
            velocity[i] -= 1
    return velocity
