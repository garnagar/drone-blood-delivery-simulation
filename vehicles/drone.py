from vehicles.vehicle import Vehicle
from geopy import distance

class Drone(Vehicle):
    def __init__(self, id, dst_center, current_battery, battery_capacity, total_carrying_capacity, charging_speed) -> None:
        super().__init__(id, dst_center, km_emissions=2.51)             #2.5056 grams of CO2/KWh
        self.current_battery = current_battery
        self.battery_capacity = battery_capacity
        self.total_carrying_capacity = total_carrying_capacity
        self.charging_speed = charging_speed

    def calculate_delivery_power_consumption(self, hospital):
        return self.get_distance_hospital(hospital) * self.km_consumption

    def charging_time(self):
        return (self.battery_capacity-self.current_battery)/self.charging_speed
    
    def get_distance_hospital(self, hospital):
        origin = (self.dst_center.location['long'], self.dst_center.location['lat'])
        destination = (hospital.location['long'], hospital.location['lat'])

        dist = distance.distance(origin, destination).km

        return round(dist, 2)
    
    def get_eta(self, hospital):
        pass