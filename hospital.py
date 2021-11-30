import simpy
import random

from config import DRONE_BLOOD_CAPACITY
from utils import min_to_str

class Hospital:

    def __init__(self, env, plot, hospitalID, long, lat, distribution_center, blood_req_tseries, mode, numb_of_res, flag):
        self.hospitalID = hospitalID
        self.plot = plot
        self.resource_amount = numb_of_res
        self.location = dict(lat=lat, long=long)
        self.distr_center = distribution_center
        self.mode = mode
        self.firstIter = flag
        env.process(self.blood_request_generator(env, blood_req_tseries, mode))

    def blood_request_generator(self, env, blood_req_tseries, mode):
        for amount in blood_req_tseries:
            if amount != 0:
                # If request is bigger than drone capacity it will be divide into smaller requests
                if mode == 'drones' and amount > DRONE_BLOOD_CAPACITY:
                    left_to_req = amount
                    while left_to_req > DRONE_BLOOD_CAPACITY:
                        env.process(self.distr_center.process_blood_request(env, self, DRONE_BLOOD_CAPACITY, mode))
                        left_to_req = left_to_req - DRONE_BLOOD_CAPACITY
                    env.process(self.distr_center.process_blood_request(env, self, left_to_req, mode))
                else:
                    env.process(self.distr_center.process_blood_request(env, self, amount, mode))
                print("{}\tBlood requested -- hospital ID: {}, amount: {}".format(min_to_str(env.now), self.hospitalID, amount))
                self.plot.add_request(env.now, amount, self.firstIter)
            yield env.timeout(1)  # Wait for 1 min


        # while True:
        #     amount = random.randint(min_amount, max_amount)
        #     env.process(self.distr_center.process_blood_request(env, self, amount))
        #     print("t={}\tBlood requested -- hospital ID: {}, amount: {}".format(str(env.now).zfill(3), self.hospitalID, amount))
        #     self.plot.add_request(env.now, amount, self.hospitalID, self.resource_amount)
        #     yield env.timeout(random.randint(min_period, max_period))  # Wait random period
