import numpy as np
import simpy

from vehicles import drone
from vehicles import ambulance
from vehicles.config import DRONE_TOTAL_CARRYING_CAPACITY, DRONE_BATTERY_CAPACITY

class DistrCenter:

    def __init__(self, env, plot, id, long, lat, dronesList=[], ambulancesList=[]):
        """ Constructor """
        self.id = id
        self.plot = plot
        self.location = dict(lat=lat, long=long)
        self.drones = dronesList
        self.ambulances = ambulancesList
        self.drones_resource = simpy.Resource(env, capacity=len(dronesList))
        self.ambulances_resource = simpy.Resource(env, capacity=len(ambulancesList))

    def get_drone_highest_battery(self):
        batteryLevel = -np.Inf
        selectedDrone = None
        for drone in self.drones:
            if drone.is_available:
                if drone.current_battery > batteryLevel:
                    selectedDrone = drone
                    batteryLevel = drone.current_battery
        return selectedDrone

    def get_ambulance(self):
        for ambulance in self.ambulances:
            if ambulance.is_available:
                return ambulance
        return None
    
    def drone_refresh(self, env):
        for drone in self.drones:
            if drone.current_battery < 0.25:
                drone.is_available = False
        
        



    def process_blood_request(self, env, hospital, amount):
        self.drone_refresh(env)

        with self.drones_resource.request() as req:
            t0 = env.now
            
            yield req
            
            drone = self.get_drone_highest_battery()
            drone.is_available = False
            drones_needed = amount / DRONE_TOTAL_CARRYING_CAPACITY
            print(drones_needed)
            
            print("initial battery: " + str(drone.charging_time()))
            
            print("t={}\tDrone leaving base -- drone ID: {}, hospital ID: {}, amount: {}, time from request: {}".format(
                str(env.now).zfill(3), drone.id, hospital.hospitalID, amount, env.now - t0))
            
            yield env.timeout(round(drone.calculate_delivery_time(hospital, self)))
            
            print("t={}\tBlood delivered -- drone ID: {}, hospital ID: {}, amount: {}, time from request: {}".format(
                str(env.now).zfill(3), drone.id, hospital.hospitalID, amount, env.now-t0))
            
            self.plot.add_deliver(env.now, amount, hospital.hospitalID, len(self.drones))
            
            yield env.timeout(round(drone.calculate_delivery_time(hospital, self)))
            
            print("t={}\tDrone back at base -- drone ID: {}, time from request: {}".format(
                str(env.now).zfill(3), drone.id, env.now - t0))

            trip_consumption= drone.calculate_delivery_power_consumption(hospital, self)
            drone.current_battery= drone.current_battery - trip_consumption
            print("trip consumption: " + str(trip_consumption))
            print("final battery: " + str(drone.current_battery))

            if drone.current_battery < DRONE_BATTERY_CAPACITY * 0.5:

                yield env.timeout(round(drone.charging_time()))
                drone.current_battery= DRONE_BATTERY_CAPACITY

                print("t={}\tDrone charged -- drone ID: {}, time from request: {}".format(
                    str(env.now).zfill(3), drone.id, env.now - t0))

            drone.is_available = True
            ## discharge drone based on the flight time / or kms
            


        #with self.ambulances_resource.request() as req:
        #    t0 = env.now
        #    yield req
        #    ambulance = self.get_ambulance()
        #    ambulance.is_available = False
        #    print("t={}\tAmbulance leaving base -- ambulance ID: {}, hospital ID: {}, amount: {}, time from request: {}".format(
        #        str(env.now).zfill(3), ambulance.id, hospital.hospitalID, amount, env.now - t0))
        #    yield env.timeout(round(ambulance.calculate_delivery_time(hospital, self)))
        #    print("t={}\tBlood delivered -- ambulance ID: {}, hospital ID: {}, amount: {}, time from request: {}".format(
        #        str(env.now).zfill(3), ambulance.id, hospital.hospitalID, amount, env.now-t0))
        #    self.plot.add_deliver(env.now, amount, hospital.hospitalID, len(self.ambulances))
        #    yield env.timeout(round(ambulance.calculate_delivery_time(hospital, self)))
        #    print("t={}\tAmbulance back at base -- ambulance ID: {}, time from request: {}".format(
        #        str(env.now).zfill(3), ambulance.id, env.now - t0))
        #    ambulance.is_available = True



            