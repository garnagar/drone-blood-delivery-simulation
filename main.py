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
from generators import generate_boold_demand_tseries_normal
from config import BLOOD_AMOUNT_MEAN_NORMAL, BLOOD_AMOUNT_SIGMA_NORMAL, BLOOD_AMOUNT_MIN_NORMAL, \
    BLOOD_AMOUNT_MAX_NORMAL, BLOOD_INTERVAL_MEAN_NORMAL, BLOOD_INTERVAL_SIGMA_NORMAL, BLOOD_INTERVAL_MIN_NORMAL, \
    BLOOD_INTERVAL_MAX_NORMAL, DIST_CENTER_LONG, DIST_CENTER_LAT

def run_testcase(hospitals_data_file, min_resources, max_resources, mode, sim_time):

    plot = Plot()
    hosp_data = pd.read_csv(hospitals_data_file)

    # Generate time series for all hospitals in advance
    blood_req = []
    for i in range(hosp_data.shape[0]):
        blood_req.append(generate_boold_demand_tseries_normal(
            BLOOD_AMOUNT_MEAN_NORMAL, BLOOD_AMOUNT_SIGMA_NORMAL, BLOOD_AMOUNT_MIN_NORMAL, BLOOD_AMOUNT_MAX_NORMAL,
            BLOOD_INTERVAL_MEAN_NORMAL, BLOOD_INTERVAL_SIGMA_NORMAL, BLOOD_INTERVAL_MIN_NORMAL, BLOOD_INTERVAL_MAX_NORMAL,
            sim_time
        ))

    # Run simulations for amounts of resources within range
    for r in range(min_resources, max_resources + 1):

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
            hospitals.append(Hospital(env, plot, row['id'], row['long'], row['lat'], dc, blood_req[i], mode, r))

        env.run(until=sim_time)

    plot.plot()

def main():

    run_testcase('resources/tc1_hospitals.csv', 3, 3, 'drones', 500)

    
if __name__ == '__main__':
    main()

