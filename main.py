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
    BLOOD_AMOUNT_MIN_CATASTROPHE, BLOOD_AMOUNT_MAX_CATASTROPHE, BLOOD_AMOUNT_SIGMA_CATASTROPHE, HOSP_DATA_FILE, MAX_RESOURCE_AMOUNT, MIN_RESOURCE_AMOUNT, TIMESTEPS


def BLOOD_AMOUNT_CATASTROPHE(args):
    pass

def gen_(hosp_data, scenario):
    # Generate time series for all hospitals in advance
    blood_req = []
    for i in range(hosp_data.shape[0]):
        if scenario == "catastrophe":
            blood_req.append(generate_blood_demand_tseries_catastrophe(
                BLOOD_AMOUNT_MEAN_CATASTROPHE, BLOOD_AMOUNT_SIGMA_CATASTROPHE, BLOOD_AMOUNT_MIN_CATASTROPHE, BLOOD_AMOUNT_MAX_CATASTROPHE,
                TIMESTEPS
            ))

        else:
            blood_req.append(generate_blood_demand_tseries_normal(
                BLOOD_AMOUNT_MEAN_NORMAL, BLOOD_AMOUNT_SIGMA_NORMAL, BLOOD_AMOUNT_MIN_NORMAL, BLOOD_AMOUNT_MAX_NORMAL,
                BLOOD_INTERVAL_MEAN_NORMAL, BLOOD_INTERVAL_SIGMA_NORMAL, BLOOD_INTERVAL_MIN_NORMAL, BLOOD_INTERVAL_MAX_NORMAL,
                TIMESTEPS
            ))
    
    return blood_req

def run_testcase(plot, hosp_data, min_resources, max_resources, mode, sim_time, blood_req):


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

    plot.plot_data()
    plot.reset_data()

def main():
    hosp_data = pd.read_csv(HOSP_DATA_FILE)

    blood_req = gen_(hosp_data, "normal")

    plot = Plot2()

    run_testcase(plot, hosp_data, MIN_RESOURCE_AMOUNT, MAX_RESOURCE_AMOUNT, 'drones', TIMESTEPS, blood_req)
    run_testcase(plot, hosp_data, MIN_RESOURCE_AMOUNT, MAX_RESOURCE_AMOUNT, 'ambulances', TIMESTEPS, blood_req)

    plot.show()


if __name__ == '__main__':
    main()

