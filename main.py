import simpy
import configparser

from distr_center import DistrCenter
from hospital import Hospital
from vehicles.drone import Drone
from vehicles.ambulance import Ambulance
from plot import Plot

def main():
    map = configparser.ConfigParser()
    map.read('resources/locations.ini')
    plt_util = Plot()

    for r in range(1, 3):
        env = simpy.Environment()

        drones = []
        for i in range(r):
            drones.append(Drone(i))

        ambulances = []
        for i in range(r):
            ambulances.append(Ambulance(i))
    
        dc = DistrCenter(env, plt_util, 0, map['DST_CENTER']['lat'], map['DST_CENTER']['long'], drones, ambulances)

        hosp0 = Hospital(env, plt_util, 0, -1.3042120313089076, 36.806186441462806, dc, r)
        hosp1 = Hospital(env, plt_util, 0, -4.06218700915241, 39.6776812700527, dc, r)

        env.run(until=500)
    
    plt_util.plot()

    
if __name__ == '__main__':
    main()

