import googlemaps

class Vehicle:
    gmaps = googlemaps.Client(key='AIzaSyC02gPus-Wzee0vswTGeuh5drh5VmL3alA')

    def __init__(self, id, dst_center, km_consumption, km_emissions, current_carrying_capacity, isAvailable=True) -> None:
        self.id = id
        self.dst_center = dst_center
        self.km_consumption = km_consumption
        self.km_emissions = km_emissions
        self.current_carrying_capacity = current_carrying_capacity
        self.isAvailable = isAvailable

    def calculate_delivery_time(self, hospital):
        pass

    def calculate_delivery_cost(self, hospital):
        pass

    def calculate_delivery_emissions(self, hospital):
        return self.km_emissions*self.get_distance_hospital(hospital)

    def get_distance_hospital(self, hospital):
        pass
