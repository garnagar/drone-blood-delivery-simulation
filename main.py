import simpy

from distr_center import DistrCenter
from hospital import Hospital
from vehicles.drone import Drone
from vehicles.ambulance import Ambulance

def main():
    env = simpy.Environment()

    drones = []
    for i in range(2):
        drones.append(Drone(i))

    ambulances = []
    for i in range(10):
        ambulances.append(Ambulance(i))

    dc = DistrCenter(env, 0, 0, 0, drones, ambulances)

    hosp0 = Hospital(env, 0, 10, 20, dc)
    hosp1 = Hospital(env, 1, 50, 60, dc)

    env.run(until=500)

    

if __name__ == '__main__':
    main()

