from vehicle import Vehicle

class Ambulance(Vehicle):
    def __init__(self, id, dst_center, fuel_consumption, fuel_capacity, current_fuel_capacity) -> None:
        super().__init__(id, dst_center)
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.current_fuel_capacity = current_fuel_capacity

    def calculate_delivery_fuel_consumption(self, hospital):
        pass