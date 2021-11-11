from vehicles.config import AMBULANCE_CONSUMPTION_PER_KM, AMBULANCE_EMISSIONS_PER_KM, AMBULANCE_FUEL_CAPACITY, AMBULANCE_TOTAL_CARRYING_CAPACITY, DIESEL_COST
from vehicles.vehicle import Vehicle

class Ambulance(Vehicle):
    gas_cost = 0.911

    def __init__(self, id) -> None:
        super().__init__(id, AMBULANCE_CONSUMPTION_PER_KM, AMBULANCE_EMISSIONS_PER_KM, AMBULANCE_TOTAL_CARRYING_CAPACITY)
        self.fuel_capacity = AMBULANCE_FUEL_CAPACITY
        self.current_fuel_capacity = AMBULANCE_FUEL_CAPACITY

    def calculate_delivery_fuel_consumption(self, hospital, dst_center):
        return self.get_distance_hospital(hospital, dst_center)*self.km_consumption

    def get_distance_hospital(self, hospital, dst_center):
        origin = str(dst_center.location['long'])+','+str(dst_center.location['lat'])
        destination = str(hospital.location['long'])+','+str(hospital.location['lat'])

        dist = Vehicle.gmaps.distance_matrix(origins=origin, destinations=destination)

        return round(dist['rows'][0]['elements'][0]['distance']['value']/1000, 2)

    # this is rtt = 2*one way
    def calculate_delivery_time(self, hospital, dst_center):
        origin = str(dst_center.location['long'])+','+str(dst_center.location['lat'])
        destination = str(hospital.location['long'])+','+str(hospital.location['lat'])

        eta = Vehicle.gmaps.distance_matrix(origins=origin, destinations=destination)
        return round(eta['rows'][0]['elements'][0]['duration']['value']/3600, 4)
    
    def calculate_delivery_cost(self, hospital, dst_center):
        return DIESEL_COST*self.calculate_delivery_fuel_consumption(hospital, dst_center)