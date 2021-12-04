from config import AMBULANCE_CONSUMPTION_PER_KM, AMBULANCE_EMISSIONS_PER_KM, AMBULANCE_EMISSIONS_PER_LITER, AMBULANCE_FUEL_CAPACITY, \
    AMBULANCE_TOTAL_CARRYING_CAPACITY, DIESEL_COST, HOURS_TO_MIN
from vehicles.vehicle import Vehicle


class Ambulance(Vehicle):
    gas_cost = 0.911

    def __init__(self, id) -> None:
        super().__init__(id, AMBULANCE_CONSUMPTION_PER_KM,
                         AMBULANCE_EMISSIONS_PER_KM, AMBULANCE_TOTAL_CARRYING_CAPACITY)
        self.fuel_capacity = AMBULANCE_FUEL_CAPACITY
        self.current_fuel_capacity = AMBULANCE_FUEL_CAPACITY

    def calculate_delivery_fuel_consumption(self, origin, destination):
        return self.get_distance(origin, destination)*self.km_consumption

    def get_distance(self, origin, destination):
        ori_coord = str(origin.location['lat']) + \
            ','+str(origin.location['long'])
        dst_coord = str(
            destination.location['lat'])+','+str(destination.location['long'])

        dist = Vehicle.gmaps.distance_matrix(
            origins=ori_coord, destinations=dst_coord)

        return round(dist['rows'][0]['elements'][0]['distance']['value']/1000, 2)

    def get_eta(self, origin, destination):
        ori_coord = str(origin.location['lat']) + \
            ','+str(origin.location['long'])
        dst_coord = str(
            destination.location['lat'])+','+str(destination.location['long'])

        eta = Vehicle.gmaps.distance_matrix(
            origins=ori_coord, destinations=dst_coord)

        return round(eta['rows'][0]['elements'][0]['duration']['value']/3600, 4) * HOURS_TO_MIN

    def calculate_delivery_cost(self, origin, destination):
        return DIESEL_COST*self.calculate_delivery_fuel_consumption(origin, destination)

    def calculate_delivery_emissions(self, origin, destination):
        return AMBULANCE_EMISSIONS_PER_LITER * self.calculate_delivery_fuel_consumption(origin, destination)
