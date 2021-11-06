from hospital import Hospital
from vehicles.vehicle import Vehicle
from geopy import distance

class Drone(Vehicle):
    elec_cost = 0.146
    def __init__(self, id, dst_center, km_consumption, km_emissions, current_carrying_capacity, battery_capacity, total_carrying_capacity, charging_speed, speed) -> None:
        super().__init__(id, dst_center, km_consumption, km_emissions, current_carrying_capacity)
        self.current_battery = battery_capacity
        self.battery_capacity = battery_capacity
        self.total_carrying_capacity = total_carrying_capacity
        self.charging_speed = charging_speed
        self.speed = speed

    def calculate_delivery_power_consumption(self, hospital):
        return self.get_distance_hospital(hospital) * self.km_consumption

    def charging_time(self):
        return (self.battery_capacity-self.current_battery)/self.charging_speed
    
    def get_distance_hospital(self, hospital):
        origin = (self.dst_center.location['long'], self.dst_center.location['lat'])
        destination = (hospital.location['long'], hospital.location['lat'])

        dist = distance.distance(origin, destination).km

        return round(dist, 2)
    
    def calculate_delivery_time(self, hospital):
        return round(self.get_distance_hospital(hospital)/self.speed, 2)

    def calculate_delivery_cost(self, hospital):
        return self.elec_cost * self.get_distance_hospital(hospital) * self.calculate_delivery_power_consumption(Hospital)