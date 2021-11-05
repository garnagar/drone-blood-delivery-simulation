from vehicle import Vehicle

class Drone(Vehicle):
    def __init__(self, id, dst_center, current_battery, battery_capacity, battery_consumption, total_carrying_capacity, charging_speed) -> None:
        super().__init__(id, dst_center)
        self.current_battery = current_battery
        self.battery_capacity = battery_capacity
        self.battery_consumption = battery_consumption
        self.total_carrying_capacity = total_carrying_capacity
        self.charging_speed = charging_speed

    def calculate_delivery_power_consumption(self, hospital):
        pass

    def charging_time(self):
        pass
