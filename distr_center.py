"""
Project: Drone Blood Delivery Simulator
File: DistribCenter.py
Author:  Lukas Kyzlik
"""
import numpy as np
import simpy

from vehicles import drone
from vehicles import ambulance

class DistrCenter:

    def __init__(self, env, id, long, lat, dronesList=[], ambulancesList=[]):
        """ Constructor """
        self.id = id
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

    def process_boold_request(self, env, hospital, amount):
        with self.drones_resource.request() as req:
            t0 = env.now
            yield req
            drone = self.get_drone_highest_battery()
            drone.is_available = False
            print("t={}\tDrone leaving base -- drone ID: {}, hospital ID: {}, amount: {}, time from request: {}".format(
                str(env.now).zfill(3), drone.id, hospital.hospitalID, amount, env.now - t0))
            yield env.timeout(round(drone.calculate_delivery_time(hospital, self)))
            print("t={}\tBlood delivered -- drone ID: {}, hospital ID: {}, amount: {}, time from request: {}".format(
                str(env.now).zfill(3), drone.id, hospital.hospitalID, amount, env.now-t0))
            yield env.timeout(round(drone.calculate_delivery_time(hospital, self)))
            print("t={}\tDrone back at base -- drone ID: {}, time from request: {}".format(
                str(env.now).zfill(3), drone.id, env.now - t0))
            drone.is_available = True



            