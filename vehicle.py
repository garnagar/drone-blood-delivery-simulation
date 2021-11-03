class Vehicle:
    def __init__(self, id, dst_center, km_consumption, km_emissions, current_carrying_capacity, max_speed, current_speed) -> None:
        self.id = id
        self.dst_center = dst_center
        self.km_consumption = km_consumption
        self.km_emissions = km_emissions
        self.current_carrying_capacity = current_carrying_capacity
        self.max_speed = max_speed
        self.current_speed = current_speed

    def calculate_delivery_time(self, hospital):
        pass

    def calculate_delivery_cost(self, hospital):
        pass

    def calculate_delivery_emissions(self, hospital):
        pass

    def get_distance_hospital(self, hospital):
        # calculates distance between self.dst_center and hospital
        pass