#!/usr/bin/env python3
import matplotlib.pyplot as plt
import simpy
import configparser
import pandas as pd

from distr_center import DistrCenter
from hospital import Hospital
from vehicles.drone import Drone
from vehicles.ambulance import Ambulance
from plot import Plot
from plot2 import Plot2
from generators import generate_blood_demand_tseries_normal, generate_blood_demand_tseries_catastrophe
from config import BLOOD_AMOUNT_MEAN_NORMAL, BLOOD_AMOUNT_SIGMA_NORMAL, BLOOD_AMOUNT_MIN_NORMAL, \
    BLOOD_AMOUNT_MAX_NORMAL, BLOOD_INTERVAL_MEAN_NORMAL, BLOOD_INTERVAL_SIGMA_NORMAL, BLOOD_INTERVAL_MIN_NORMAL, \
    BLOOD_INTERVAL_MAX_NORMAL, DIST_CENTER_LONG, DIST_CENTER_LAT, BLOOD_AMOUNT_MEAN_CATASTROPHE, \
    BLOOD_AMOUNT_MIN_CATASTROPHE, BLOOD_AMOUNT_MAX_CATASTROPHE, BLOOD_AMOUNT_SIGMA_CATASTROPHE, TIMESTEPS

def get_sim_data(hosp_data_file, scenario):

    # Get hospital data from file
    hosp_data = pd.read_csv(hosp_data_file)

    # Generate time series for all hospitals in advance
    blood_req = []
    for i in range(hosp_data.shape[0]):
        if scenario == "catastrophe":
            blood_req.append(generate_blood_demand_tseries_catastrophe(
                BLOOD_AMOUNT_MEAN_CATASTROPHE, BLOOD_AMOUNT_SIGMA_CATASTROPHE, BLOOD_AMOUNT_MIN_CATASTROPHE, BLOOD_AMOUNT_MAX_CATASTROPHE,
                TIMESTEPS
            ))
        elif scenario == "normal":
            blood_req.append(generate_blood_demand_tseries_normal(
                BLOOD_AMOUNT_MEAN_NORMAL, BLOOD_AMOUNT_SIGMA_NORMAL, BLOOD_AMOUNT_MIN_NORMAL, BLOOD_AMOUNT_MAX_NORMAL,
                BLOOD_INTERVAL_MEAN_NORMAL, BLOOD_INTERVAL_SIGMA_NORMAL, BLOOD_INTERVAL_MIN_NORMAL, BLOOD_INTERVAL_MAX_NORMAL,
                TIMESTEPS
            ))
        else:
            raise ValueError("'{}' is not valid scenario type")

    return hosp_data, blood_req

def run_testcase(plot, hosp_data, blood_req, min_resources, max_resources, mode, sim_time):

    firstIter = True

    # Run simulations for amounts of resources within range
    for r in range(min_resources, max_resources + 1):

        if r > min_resources:
            firstIter = False

        print("Starting simulation with {} resource(s) in mode '{}'".format(r, mode))
        env = simpy.Environment()

        drones = []
        for i in range(r):
            drones.append(Drone(i))
        ambulances = []
        for i in range(r):
            ambulances.append(Ambulance(i))

        dc = DistrCenter(env, plot, 0, DIST_CENTER_LONG, DIST_CENTER_LAT, drones, ambulances, mode)

        hospitals = []
        for i, row in hosp_data.iterrows():
            hospitals.append(Hospital(env, plot, int(row['id']), row['long'], row['lat'], dc, blood_req[i], mode, r, firstIter))

        env.run(until=sim_time)

    plot.plot_data(mode)
    plot.reset_data()

def main():

    # Edit this code to produce graphs you need:

    # 1. Select what will be plotted by setting enables
    plot = Plot2(enable_blood=True, enable_power=False, enable_fuel=False, enable_cost=True, enable_emissions=True, enable_travel=False)

    # 2. Select CSV file with hospital data and blood demand scenario as 'normal' or 'catastrophe'
    hosp_data, blood_req = get_sim_data('resources/tc4.csv', 'catastrophe')

    # 3. Select simulations to run. Each run_testcase() will produce data for each resource amount and add them to plot
    run_testcase(plot, hosp_data, blood_req, 15, 15, 'drones', TIMESTEPS)
    run_testcase(plot, hosp_data, blood_req, 1, 1, 'ambulances', TIMESTEPS)

    # 4. Profit
    plot.show()

if __name__ == '__main__':
    main()

