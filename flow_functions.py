import numpy as np

def position_update(road, position, velocity, road_length):
    '''function that updates position with accordance to velocity
    also creates road array that has values of velocities in corresponding position'''

    #calculate new position and store it in the same array
    position = (position + velocity)%road_length

    return position

def speed_update(position, velocity, v_max, road_length, rand_slow_chance, num_cars):
    '''function that updates velocities according to rules'''

    #how far is the next car
    space_next_car = np.diff(position, append=position[0])%road_length
    #generate uniform random intigers with probability for any given integer equal rand_slow_chance
    rand_slow = np.random.random_integers(0, int(1/rand_slow_chance), size=num_cars)
    #is there more than 1 car
    many_cars = num_cars > 1

    velocity[velocity < v_max] += 1
    velocity[space_next_car <= velocity] =  space_next_car[space_next_car <= velocity] - 1
    velocity -= np.random.rand(num_cars) < rand_slow_chance
    velocity[velocity < 0] = 0

    return velocity

def counting_cars(position, velocity, road_length, car_count):
    "counting cars that have gone from the end of the road"
    new_car_count = position[(position + velocity - (road_length-1)) > 0].size
    car_count += new_car_count
    return car_count

def measure_flow(time, car_count):
    "calculating flow value"
    flow = car_count/time
    return flow
