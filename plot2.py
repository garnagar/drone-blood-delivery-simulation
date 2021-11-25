import numpy as np
import matplotlib.pyplot as plt

class Plot2():

    def __init__(self):
        self.requestedY = [0]
        self.requestedX = [0]
        self.requested_total = 0

        self.deliveredY = {}
        self.deliveredX = {}
        self.delivered_total = {}

    def add_request(self, step, amount, flag):
        if flag is False:
            return
        self.requestedX.append(step)
        self.requested_total += amount
        self.requestedY.append(self.requested_total)

    def add_deliver(self, step, amount, resource_amount):
        if resource_amount not in self.deliveredX.keys():
            self.deliveredX.update({resource_amount: [0]})
        self.deliveredX[resource_amount].append(step)

        if resource_amount not in self.delivered_total.keys():
            self.delivered_total.update({resource_amount: 0})
        self.delivered_total[resource_amount] += amount

        if resource_amount not in self.deliveredY.keys():
            self.deliveredY.update({resource_amount: [0]})
        self.deliveredY[resource_amount].append(self.delivered_total[resource_amount])

    def add_consumptions(self, step, consumption, resource_amount):
        pass

    def plot(self):
        plt.plot(self.requestedX, self.requestedY, '-x', label="Requested")
        print(self.deliveredX)
        for r in self.deliveredX:
            plt.plot(self.deliveredX[r], self.deliveredY[r], '--x', label="Delivered, resources: {}".format(r))
        plt.xlabel("Time [min]")
        plt.ylabel("Blood units")
        plt.legend()
        plt.show()


