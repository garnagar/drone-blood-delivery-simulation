import matplotlib.pyplot as plt
import pandas as pd

class Plot:
    def __init__(self):
        self.requests = {}                  
        self.deliveries = {}
        self.emissions = {}
        self.costs = {}

    def add_request(self, step, amount, flag):
        if (flag is False):
            return

        l = list(self.requests)

        if not self.requests:
            self.requests[step] = amount
        else:
            self.requests[step] = l[-1] + amount

    def add_deliver(self, step, amount, resource_amount):

        if resource_amount not in self.deliveries.keys():
            self.deliveries[resource_amount] = {}

        l = list(self.deliveries[resource_amount])

        if len(l) == 0:
            self.deliveries[resource_amount][step] = amount
        
        else:
            self.deliveries[resource_amount][step] = l[-1] + amount

    def plot(self):
        df = pd.Series(self.requests, name='Requested Blood Units')
        df.index.name = 'Time'
        df.reset_index()
        df.plot(legend=True).set_ylabel("Blood Units")
        
        for r_amount in self.deliveries.keys():
            df = pd.Series(self.deliveries[r_amount], name='Delivered Blood Units; Resources: ' + str(r_amount))
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


        