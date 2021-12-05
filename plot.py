import numpy as np
import matplotlib.pyplot as plt


class Plot():

    def __init__(self, enable_blood=True, enable_power=False, enable_fuel=False, enable_cost=False, enable_emissions=False, enable_travel=False):
        self.enable = np.array(
            [enable_blood, enable_power, enable_fuel, enable_cost, enable_emissions, enable_travel])
        self.fig, self.axs = plt.subplots(np.count_nonzero(self.enable))
        self.isFirst = True

        self.requestedX = [0]
        self.requestedY = [0]
        self.requested_total = 0

        self.deliveredX = {}
        self.deliveredY = {}
        self.delivered_total = {}

        self.power_consumptionX = {}
        self.power_consumptionY = {}
        self.power_consumption_total = {}

        self.fuel_consumptionX = {}
        self.fuel_consumptionY = {}
        self.fuel_consumption_total = {}

        self.costX = {}
        self.costY = {}
        self.cost_total = {}

        self.emissionX = {}
        self.emissionY = {}
        self.emission_total = {}

        self.travelX = {}
        self.travelY = {}
        self.travel_total = {}

    def __add_data_point(self, x_data, y_data, total, step, value, resource_amount):
        if resource_amount not in x_data.keys():
            x_data.update({resource_amount: [0]})
        x_data[resource_amount].append(step)

        if resource_amount not in total.keys():
            total.update({resource_amount: 0})
        total[resource_amount] += value

        if resource_amount not in y_data.keys():
            y_data.update({resource_amount: [0]})
        y_data[resource_amount].append(total[resource_amount])

    def __plot_subplot(self, subplt, data_x, data_y, style, ylabel, legend_label, mode_label):
        for r in data_x:
            subplt.plot(data_x[r], data_y[r], style, label="{}{} {}".format(
                legend_label, r, mode_label))
        if ylabel is not None:
            subplt.set(ylabel=ylabel)
        subplt.legend()

    def add_request(self, step, amount, flag):
        if flag is False:
            return
        self.requestedX.append(step)
        self.requested_total += amount
        self.requestedY.append(self.requested_total)

    def add_delivery(self, step, amount, resource_amount):
        self.__add_data_point(self.deliveredX, self.deliveredY, self.delivered_total,
                              step, amount, resource_amount)

    def add_emission(self, step, emission, resource_amount):
        self.__add_data_point(self.emissionX, self.emissionY, self.emission_total,
                              step, emission, resource_amount)

    def add_travel(self, step, value, resource_amount):
        self.__add_data_point(self.travelX, self.travelY, self.travel_total,
                              step, value, resource_amount)

    def add_cost(self, step, cost, resource_amount):
        self.__add_data_point(self.costX, self.costY, self.cost_total,
                              step, cost, resource_amount)

    def add_power_consumption(self, step, consumption, resource_amount):
        self.__add_data_point(self.power_consumptionX, self.power_consumptionY, self.power_consumption_total,
                              step, consumption, resource_amount)

    def add_fuel_consumption(self, step, consumption, resource_amount):
        self.__add_data_point(self.fuel_consumptionX, self.fuel_consumptionY, self.fuel_consumption_total,
                              step, consumption, resource_amount)

    def plot_data(self, mode):

        n = 0

        if self.enable[0]:
            if self.isFirst:
                self.axs[n].plot(self.requestedX, self.requestedY,
                                 'k-x', label="requested")
            self.isFirst = False
            self.__plot_subplot(
                self.axs[n], self.deliveredX, self.deliveredY, '-x', "Blood units", "delivered, ", mode)

        if self.enable[1]:
            n += 1
            self.__plot_subplot(self.axs[n], self.power_consumptionX,
                                self.power_consumptionY, '-x', "Power [kWh]", "", mode)
        if self.enable[2]:
            n += 1
            self.__plot_subplot(self.axs[n], self.fuel_consumptionX,
                                self.fuel_consumptionY, '-x', "Fuel [L]", "", mode)
        if self.enable[3]:
            n += 1
            self.__plot_subplot(
                self.axs[n], self.costX, self.costY, '-x', "Cost [€]", "", mode)
        if self.enable[4]:
            n += 1
            self.__plot_subplot(
                self.axs[n], self.emissionX, self.emissionY, '-x', "Emissions [kg of CO2]", "", mode)
        if self.enable[5]:
            n += 1
            self.__plot_subplot(
                self.axs[n], self.travelX, self.travelY, '-x', 'Distance traveled [km]', "", mode)

        self.axs[-1].set(xlabel='Time [min]')

    def show(self):
        plt.show()

    def reset_data(self):
        self.requestedX = [0]
        self.requestedY = [0]
        self.requested_total = 0

        self.deliveredX = {}
        self.deliveredY = {}
        self.delivered_total = {}

        self.power_consumptionX = {}
        self.power_consumptionY = {}
        self.power_consumption_total = {}

        self.fuel_consumptionX = {}
        self.fuel_consumptionY = {}
        self.fuel_consumption_total = {}

        self.costX = {}
        self.costY = {}
        self.cost_total = {}

        self.emissionX = {}
        self.emissionY = {}
        self.emission_total = {}

        self.travelX = {}
        self.travelY = {}
        self.travel_total = {}
