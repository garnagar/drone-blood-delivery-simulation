import numpy as np
import simpy

from config import DRONE_BATTERY_CAPACITY, DRONE_MIN_SAFE_BATTERY
from utils import min_to_str

class DistrCenter:

    def __init__(self, env, plot, id, long, lat, drones_list=[], ambulances_list=[], mode='drones'):
        self.id = id
        self.plot = plot
        self.location = dict(lat=lat, long=long)
        self.drones = drones_list
        self.ambulances = ambulances_list
        self.drones_resource = simpy.Resource(env, capacity=len(drones_list))
        self.ambulances_resource = simpy.Resource(env, capacity=len(ambulances_list))
        self.mode = mode

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

    def process_blood_request(self, env, hospital, amount, mode):
        """ Processes blood request by dispatching Vehicle and managing its return to Distribution Centre """

        # Drone simulation run
        if mode == 'drones':
            res_amount = len(self.drones)
            with self.drones_resource.request() as req:
                t0 = env.now  # Get time stamp
                yield req  # Wait until drone is available
                # Get drone
                drone = self.get_drone_highest_battery()
                drone.is_available = False

                # Leave base
                print("{}\tDrone leaving base -- drone ID: {}, hospital ID: {}, amount: {}, time from request: {}".format(
                        min_to_str(env.now), drone.id, hospital.hospitalID, amount, env.now - t0))
                yield env.timeout(drone.calculate_delivery_time(hospital, self))

                # Deliver blood
                print("{}\tBlood delivered -- drone ID: {}, hospital ID: {}, amount: {}, time from request: {}".format(
                        min_to_str(env.now), drone.id, hospital.hospitalID, amount, env.now - t0))
                self.plot.add_deliver(env.now, amount, res_amount)  # Add point to plot
                yield env.timeout(drone.calculate_delivery_time(hospital, self))

                # Return to base
                trip_consumption = drone.calculate_delivery_power_consumption(hospital, self)     
                trip_cost = drone.calculate_delivery_cost(hospital, self)
                trip_emission = drone.calculate_delivery_emissions(hospital, self)
                
                self.plot.add_consumptions(env.now, trip_consumption, res_amount)
                self.plot.add_cost(env.now, trip_cost, res_amount)
                self.plot.add_emission(env.now, trip_emission, res_amount)

                drone.current_battery = round(drone.current_battery - trip_consumption, 5)  # Update battery status
                print("{}\tDrone back at base -- drone ID: {}, battery left: {} kWh, time from request: {},".format(
                    min_to_str(env.now), drone.id, drone.current_battery, env.now - t0))

                # Recharge if battery is below min safe level
                if drone.current_battery < DRONE_MIN_SAFE_BATTERY:
                    yield env.timeout(drone.charging_time())
                    drone.current_battery = DRONE_BATTERY_CAPACITY
                    print("{}\tDrone charged -- drone ID: {}, time from request: {}".format(
                        min_to_str(env.now), drone.id, env.now - t0))

                drone.is_available = True

        # Ambulance simulation run
        elif mode == 'ambulances':
            res_amount = len(self.ambulances)
            with self.ambulances_resource.request() as req:
               t0 = env.now # Get time stamp
               yield req # Wait until ambulance is available
               # Get ambulance
               ambulance = self.get_ambulance()
               ambulance.is_available = False

               # Leave base
               print("t={}\tAmbulance leaving base -- ambulance ID: {}, hospital ID: {}, amount: {}, time from request: {}".format(
                   str(env.now).zfill(3), ambulance.id, hospital.hospitalID, amount, env.now - t0))
               yield env.timeout(round(ambulance.calculate_delivery_time(hospital, self)))

               # Deliver blood
               print("t={}\tBlood delivered -- ambulance ID: {}, hospital ID: {}, amount: {}, time from request: {}".format(
                   str(env.now).zfill(3), ambulance.id, hospital.hospitalID, amount, env.now-t0))
               self.plot.add_deliver(env.now, amount, len(self.ambulances)) # Add point to plot
               yield env.timeout(round(ambulance.calculate_delivery_time(hospital, self)))

               # Return to base
               print("t={}\tAmbulance back at base -- ambulance ID: {}, time from request: {}".format(
                   str(env.now).zfill(3), ambulance.id, env.now - t0))

               trip_consumption = ambulance.calculate_delivery_fuel_consumption(hospital, self)     
               trip_cost = ambulance.calculate_delivery_cost(hospital, self)
               trip_emission = ambulance.calculate_delivery_emissions(hospital, self)
               
               self.plot.add_consumptions(env.now, trip_consumption, res_amount)
               self.plot.add_cost(env.now, trip_cost, res_amount)
               self.plot.add_emission(env.now, trip_emission, res_amount)

               ambulance.is_available = True

        else:
            raise ValueError("{} is not valid simulation mode".format(mode))



            