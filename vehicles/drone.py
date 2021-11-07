from hospital import Hospital
from vehicles.config import DRONE_BATTERY_CAPACITY, DRONE_CHARGING_SPEED, DRONE_CONSUMPTION_PER_KM, DRONE_CRUISING_SPEED, DRONE_EMISSIONS_PER_KM, DRONE_TOTAL_CARRYING_CAPACITY, ELECTRICITY_COST
from vehicles.vehicle import Vehicle
from geopy import distance

class Drone(Vehicle):
    elec_cost = 0.146
    def __init__(self, id, dst_center) -> None:
        super().__init__(id, dst_center, DRONE_CONSUMPTION_PER_KM, DRONE_EMISSIONS_PER_KM, DRONE_TOTAL_CARRYING_CAPACITY)
        self.current_battery = DRONE_BATTERY_CAPACITY
        self.battery_capacity = DRONE_BATTERY_CAPACITY
        self.total_carrying_capacity = DRONE_TOTAL_CARRYING_CAPACITY
        self.charging_speed = DRONE_CHARGING_SPEED
        self.speed = DRONE_CRUISING_SPEED

    def calculate_delivery_power_consumption(self, hospital):
        return self.get_distance_hospital(hospital) * self.km_consumption

    def charging_time(self):
        return (self.battery_capacity-self.current_battery)/self.charging_speed
    
    def get_distance_hospital(self, hospital):
        origin = (self.dst_center.location['long'], self.dst_center.location['lat'])
        destination = (hospital.location['long'], hospital.location['lat'])

        dist = distance.distance(origin, destination).km

        return round(dist, 2)
    
    # this is rtt = 2*one way
    def calculate_delivery_time(self, hospital):
        return 2*round(self.get_distance_hospital(hospital)/self.speed, 2)

    def calculate_delivery_cost(self, hospital):
        return ELECTRICITY_COST * self.calculate_delivery_power_consumption(Hospital)