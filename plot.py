import matplotlib.pyplot as plt
import pandas as pd

class Plot:
    def __init__(self):
        self.requests = {}                  
        self.delivers = {}                  # hospital: resource_amount: step: amount
        self.partial_req = {}
        self.partial_del = {}
        self.emissions = []
        self.costs = []

    def add_request(self, step, amount, hospital, resource_amount):
        if hospital not in self.requests.keys():
            self.requests[hospital] = {}
            self.partial_req[hospital] = {}
        
        if resource_amount not in self.requests[hospital].keys():
            self.requests[hospital][resource_amount] = {}
            self.partial_req[hospital][resource_amount] = {}

        l = list(self.requests[hospital][resource_amount])

        self.partial_req[hospital][resource_amount][step] = amount
        if len(l) == 0:
            self.requests[hospital][resource_amount][step] = amount
        
        else:
            self.requests[hospital][resource_amount][step] = l[-1] + amount

    def add_deliver(self, step, amount, hospital, resource_amount):
        if hospital not in self.delivers.keys():
            self.delivers[hospital] = {}
            self.partial_del[hospital] = {}
        
        if resource_amount not in self.delivers[hospital].keys():
            self.delivers[hospital][resource_amount] = {}
            self.partial_del[hospital][resource_amount] = {}

        l = list(self.delivers[hospital][resource_amount])

        self.partial_del[hospital][resource_amount][step] = amount
        if len(l) == 0:
            self.delivers[hospital][resource_amount][step] = amount
        
        else:
            self.delivers[hospital][resource_amount][step] = l[-1] + amount

    def plot(self):
        for hospital in self.requests.keys():
            for r_amount in self.requests[hospital].keys():
                df = pd.Series(self.requests[hospital][r_amount], name='Requested Blood Units - Hospital: ' + str(hospital))
                df.index.name = 'Time'
                df.reset_index()
                df.plot(legend=True).set_ylabel("Blood Units")
        
        for hospital in self.delivers.keys():
            for r_amount in self.delivers[hospital].keys():
                df = pd.Series(self.delivers[hospital][r_amount], name='Delivered Blood Units - Hospital: ' + str(hospital) + "; Resources: " + str(r_amount))
                df.index.name = 'Time'
                df.reset_index()
                df.plot(legend=True).set_ylabel("Blood Units")

        #for hospital in self.partial_req.keys():
        #    df = pd.Series(self.partial_req[hospital], name='Partials Blood Units Requests - Hospital: ' + str(hospital))
        #    df.index.name = 'Time'
        #    df.reset_index()
        #    df.plot(legend=True).set_ylabel("Blood Units")
        
        #for hospital in self.partial_del.keys():
        #    df = pd.Series(self.partial_del[hospital], name='Partial Blood Units Deliveries - Hospital: ' + str(hospital))
        #    df.index.name = 'Time'
        #    df.reset_index()
        #    df.plot(legend=True).set_ylabel("Blood Units")

        plt.show()


        