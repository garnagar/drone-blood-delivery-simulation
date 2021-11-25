import numpy as np
import matplotlib.pyplot as plt

class Plot2():

    def __init__(self, mode):
        self.mode = mode
        self.requestedY = [0]
        self.requestedX = [0]
        self.requested_total = 0

        self.deliveredY = {}
        self.deliveredX = {}
        self.delivered_total = {}

        self.consumptionY = {}
        self.consumptionX = {}
        self.consumption_total = {}

        self.costY = {}
        self.costX = {}
        self.cost_total = {}

        self.emissionY = {}
        self.emissionX = {}
        self.emission_total = {}

    def add_emission(self, step, emission, resource_amount):
        if resource_amount not in self.emissionX.keys():
            self.emissionX.update({resource_amount: [0]})
        self.emissionX[resource_amount].append(step)

        if resource_amount not in self.emission_total.keys():
            self.emission_total.update({resource_amount: 0})
        self.emission_total[resource_amount] += emission

        if resource_amount not in self.emissionY.keys():
            self.emissionY.update({resource_amount: [0]})
        self.emissionY[resource_amount].append(self.emission_total[resource_amount])


    def add_cost(self, step, cost, resource_amount):
        if resource_amount not in self.costX.keys():
            self.costX.update({resource_amount: [0]})
        self.costX[resource_amount].append(step)

        if resource_amount not in self.cost_total.keys():
            self.cost_total.update({resource_amount: 0})
        self.cost_total[resource_amount] += cost

        if resource_amount not in self.costY.keys():
            self.costY.update({resource_amount: [0]})
        self.costY[resource_amount].append(self.cost_total[resource_amount])


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
        if self.mode == 'ambulances':
            consumption_unit = 'l (liters)'
        else:
            consumption_unit = 'kWh (kilowatt-hour)'

        fig, axs = plt.subplots(4)
        fig.suptitle('Blood delivering through '+str(self.mode))
        
        axs[0].plot(self.requestedX, self.requestedY, '-x', label="Requested")
        for r in self.deliveredX:
            axs[0].plot(self.deliveredX[r], self.deliveredY[r], '--x', label="Delivered, resources: {}".format(r))
        
        axs[0].set(ylabel='Blood units')
        axs[0].legend()

        for r in self.consumptionX:
            axs[1].plot(self.consumptionX[r], self.consumptionY[r], '-x', label="Consumption, resources: {}".format(r))
        axs[1].set(ylabel=consumption_unit)
        axs[1].legend()

        for r in self.costX:
            axs[2].plot(self.costX[r], self.costY[r], '-x', label="Cost, resources: {}".format(r))
        axs[2].set(ylabel='€')
        axs[2].legend()

        for r in self.emissionX:
            axs[3].plot(self.emissionX[r], self.emissionY[r], '-x', label="Emissions, resources: {}".format(r))
        axs[3].set(xlabel='Time [min]', ylabel='g of CO2')
        axs[3].legend()
