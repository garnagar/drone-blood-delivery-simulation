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

        self.consumptionY = {}
        self.consumptionX = {}
        self.consumption_total = {}

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
        if resource_amount not in self.consumptionX.keys():
            self.consumptionX.update({resource_amount: [0]})
        self.consumptionX[resource_amount].append(step)

        if resource_amount not in self.consumption_total.keys():
            self.consumption_total.update({resource_amount: 0})
        self.consumption_total[resource_amount] += consumption

        if resource_amount not in self.consumptionY.keys():
            self.consumptionY.update({resource_amount: [0]})
        self.consumptionY[resource_amount].append(self.consumption_total[resource_amount])
        
    def plot(self):
        fig, axs = plt.subplots(2)
        fig.suptitle('MBSE')
        
        axs[0].plot(self.requestedX, self.requestedY, '-x', label="Requested")
        print(self.deliveredX)
        for r in self.deliveredX:
            axs[0].plot(self.deliveredX[r], self.deliveredY[r], '--x', label="Delivered, resources: {}".format(r))
        
        axs[0].set(xlabel='Time [min]', ylabel='Blood units')
        axs[0].legend()

        for r in self.consumptionX:
            axs[1].plot(self.consumptionX[r], self.consumptionY[r], '-x', label="Consumption, resources: {}".format(r))
        axs[1].set(xlabel='Time [min]', ylabel='kWh')
        axs[1].legend()
        plt.show()

        

