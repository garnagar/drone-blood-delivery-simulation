from vehicles.vehicle import Vehicle

class Ambulance(Vehicle):
    def __init__(self, id, dst_center, fuel_consumption=None, fuel_capacity=None, current_fuel_capacity=None) -> None:
        super().__init__(id, dst_center, km_emissions=21.60)
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.current_fuel_capacity = current_fuel_capacity
        # self.avg_speed = avg_speed

    def calculate_delivery_fuel_consumption(self, hospital):
        pass

    def get_distance_hospital(self, hospital):
        origin = str(self.dst_center.location['long'])+','+str(self.dst_center.location['lat'])
        destination = str(hospital.location['long'])+','+str(hospital.location['lat'])

        dist = Vehicle.gmaps.distance_matrix(origins=origin, destinations=destination)

        return round(dist['rows'][0]['elements'][0]['distance']['value']/1000, 2)


    def get_eta(self, hospital):
        origin = str(self.dst_center.location['long'])+','+str(self.dst_center.location['lat'])
        destination = str(hospital.location['long'])+','+str(hospital.location['lat'])

        eta = Vehicle.gmaps.distance_matrix(origins=origin, destinations=destination)

        return round(eta['rows'][0]['elements'][0]['duration']['value']/3600, 4)