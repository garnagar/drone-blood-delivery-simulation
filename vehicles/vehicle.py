import googlemaps


class Vehicle:
    gmaps = googlemaps.Client(key='AIzaSyC02gPus-Wzee0vswTGeuh5drh5VmL3alA')

    def __init__(self, id, km_consumption, km_emissions, total_carrying_capacity, is_available=True) -> None:
        self.id = id
        self.km_consumption = km_consumption
        self.km_emissions = km_emissions
        self.total_carrying_capacity = total_carrying_capacity
        self.current_carrying_capacity = total_carrying_capacity
        self.is_available = is_available

    def get_eta(self, origin, destination):
        pass

    def calculate_delivery_cost(self, origin, destination):
        pass

    def calculate_delivery_emissions(self, origin, destination):
        pass

    def get_distance(self, origin, destination):
        pass
