"""
Project: Drone Blood Delivery Simulator
File: DistribCenter.py
Author:  Lukas Kyzlik
"""
import numpy as np

class DistrCenter:
    """ TODO """

    def __init__(self, id, long, lat, hospitalList=[], dronesList=[], ambulancesList=[]):
        """ Constructor """
        self.id = id
        self.location = dict(lat=lat, long=long)
        self.hospitals = hospitalList
        self.drones = dronesList
        self.ambulances = ambulancesList
        self.booldRequests = []

    def getDroneHighestBattery(self):
        """ TODO """
        batteryLevel = -np.Inf
        selectedDrone = None
        for drone in self.drones:
            if drone.isAvailable:
                if drone.currentBattery > batteryLevel:
                    selectedDrone = drone
                    batteryLevel = drone.currentBattery
        return selectedDrone

    def getAmbulance(self):
        for ambulance in self.ambulances:
            if ambulance.isAvailable:
                return ambulance
        return None

    def sendAmbulance(self, hosptalId, bloodAmount):
        """ TODO """
        ambulance = self.getAmbulance()
        if ambulance is None:
            return False
        ambulance.isAvailable = False
        # TODO: activate return mechanism
        return True

    def sendDrone(self, hosptalId, bloodAmount):
        """ TODO """
        drone = self.getDroneHighestBattery()
        if drone is None:
            return False
        drone.isAvailable = False
        # TODO: activate return mechanism
        return True

    def acceptBloodRequest(self, hospitalId, bloodAmount):
        self.booldRequests.append(dict(hospId=hospitalId, amount=bloodAmount))

    def advanceSim(self):
        for req in self.booldRequests:
            self.sendDrone(req['hospId'], req['amount'])
            