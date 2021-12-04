import matplotlib.pyplot as plt
import pandas as pd


class Plot:
    def __init__(self):
        self.requests = {}
        self.deliveries = {}
        self.consumptions = {}

    def add_consumptions(self, step, consumption, resource_amount):
        if resource_amount not in self.consumptions.keys():
            self.consumptions[resource_amount] = {}

        l = list(self.consumptions[resource_amount])

        if len(l) == 0:
            self.consumptions[resource_amount][step] = consumption

        else:
            self.consumptions[resource_amount][step] = l[-1] + consumption

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
            df = pd.Series(
                self.deliveries[r_amount], name='Delivered Blood Units; Resources: ' + str(r_amount))
            df.index.name = 'Time'
            df.reset_index()
            df.plot(legend=True).set_ylabel("Blood Units")

        plt.show()

        for r_amount in self.consumptions.keys():
            df = pd.Series(
                self.consumptions[r_amount], name='Consumptions; Resources: ' + str(r_amount))
            df.index.name = 'Time'
            df.reset_index()
            df.plot(legend=True).set_ylabel("kWh")  # or liters for ambulances

        plt.show()
