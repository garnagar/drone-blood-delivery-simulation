import simpy
import random

class Hospital:

    def __init__(self, env, hospitalID, long, lat, distribution_center=None):
        self.hospitalID = hospitalID
        # self.current_level_of_blood = current_level_of_blood
        # self.max_level_of_blood = max_level_of_blood
        # self.min_safe_level_of_blood = min_safe_level_of_blood
        self.location = dict(lat=lat, long=long)
        self.distr_center = distribution_center
        env.process(self.blood_request_generator(env, 5, 10, 1, 4))

    # def consume_blood(self, amount):
    #     self.current_level_of_blood = self.current_level_of_blood - amount

    def blood_request_generator(self, env, min_period, max_period, min_amount, max_amount):
        while True:
            amount = random.randint(min_amount, max_amount)
            env.process(self.distr_center.process_blood_request(env, self, amount))
            print("t={}\tBlood requested -- hospital ID: {}, amount: {}".format(str(env.now).zfill(3), self.hospitalID, amount))
            yield env.timeout(random.randint(min_period, max_period))  # Wait random period
