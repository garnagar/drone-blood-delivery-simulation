class Hospital:

    def __init__(self, hospitalID, longitude, latitude, current_level_of_blood=None, max_level_of_blood=None, min_safe_level_of_blood=None, dc=None):
        self.hospitalID = hospitalID
        self.current_level_of_blood = current_level_of_blood
        self.max_level_of_blood = max_level_of_blood
        self.min_safe_level_of_blood = min_safe_level_of_blood
        self.longitude = longitude
        self.latitude = latitude
        self.distribution_center = dc

    def consume_blood(self, amount):
        self.current_level_of_blood = self.current_level_of_blood - amount

    def request_blood(self,amount):
        pass

#h1 = Hospital(1, 50, 100, 1, 13, 25)
#print(h1.current_level_of_blood)
#h1.consume_blood(20)
#print(h1.current_level_of_blood)
