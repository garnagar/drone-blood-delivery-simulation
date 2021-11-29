from config import DRONE_BATTERY_CAPACITY, DRONE_CHARGING_SPEED, DRONE_CONSUMPTION_PER_KM, DRONE_CRUISING_SPEED, \
                   DRONE_EMISSIONS_PER_KM, DRONE_EMISSIONS_PER_KWH, DRONE_TOTAL_CARRYING_CAPACITY, ELECTRICITY_COST, HOURS_TO_MIN
from vehicles.vehicle import Vehicle
from geopy import distance

class Drone(Vehicle):
    elec_cost = 0.146
    def __init__(self, id) -> None:
        super().__init__(id, DRONE_CONSUMPTION_PER_KM, DRONE_EMISSIONS_PER_KM, DRONE_TOTAL_CARRYING_CAPACITY)
        self.current_battery = DRONE_BATTERY_CAPACITY
        self.battery_capacity = DRONE_BATTERY_CAPACITY
        self.total_carrying_capacity = DRONE_TOTAL_CARRYING_CAPACITY
        self.charging_speed = DRONE_CHARGING_SPEED
        self.speed = DRONE_CRUISING_SPEED

    def calculate_delivery_power_consumption(self, hospital, dst_center):
        return self.get_distance(hospital, dst_center) * self.km_consumption

    def charging_time(self):
        return ((self.battery_capacity-self.current_battery)/self.charging_speed) * HOURS_TO_MIN
    
    def get_distance(self, origin, destination):
        ori_coord = (origin.location['lat'], origin.location['long'])
        dst_coord = (destination.location['lat'], destination.location['long'])
        
        dist = distance.distance(ori_coord, dst_coord).km

        return round(dist, 2)


    def get_eta(self, origin, destination):
        return round(self.get_distance(origin, destination)/self.speed, 2) * HOURS_TO_MIN

    def calculate_delivery_cost(self, hospital, dst_center):
        return ELECTRICITY_COST * self.calculate_delivery_power_consumption(hospital, dst_center)
    
    def calculate_delivery_emissions(self, hospital, dst_center):
        return DRONE_EMISSIONS_PER_KWH * self.calculate_delivery_power_consumption(hospital, dst_center)