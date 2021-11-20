import simpy
import configparser

from distr_center import DistrCenter
from hospital import Hospital
from vehicles.drone import Drone
from vehicles.ambulance import Ambulance

def main():
    map = configparser.ConfigParser()
    map.read('resources/locations.ini')
    env = simpy.Environment()

    drones = []
    for i in range(5):
        drones.append(Drone(i))

    ambulances = []
    for i in range(5):
        ambulances.append(Ambulance(i))

    dc = DistrCenter(env, 0, map['DST_CENTER']['lat'], map['DST_CENTER']['long'], drones, ambulances)

    # hosp0 = Hospital(env, 0, 10, 20, dc)
    # hosp1 = Hospital(env, 1, 50, 60, dc)

    hosp0 = Hospital(env, 0, -1.3042120313089076, 36.806186441462806, dc)
    hosp1 = Hospital(env, 0, -4.06218700915241, 39.6776812700527, dc)

    env.run(until=500)

    

if __name__ == '__main__':
    main()

