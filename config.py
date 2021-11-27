# Drones
DRONE_BATTERY_CAPACITY = 1.25               # kWh
DRONE_TOTAL_CARRYING_CAPACITY = 1.75        # kg
DRONE_CHARGING_SPEED = 0.5                  # h 0% -> 100%
DRONE_CRUISING_SPEED = 101                  # km/h
DRONE_CONSUMPTION_PER_KM = 0.00833          # kWh / km (1.25 kWh / 150 km)
DRONE_EMISSIONS_PER_KM = 2.51               # grams of CO2 / km
DRONE_MIN_SAFE_BATTERY = 0.25               # kWh
ELECTRICITY_COST = 0.146                    # € / kWh
DRONE_BLOOD_CAPACITY = 2                    # blood units
DRONE_EMISSIONS_PER_KWH = 0.386             # kg of CO2 per kWh

# Ambulances
AMBULANCE_TOTAL_CARRYING_CAPACITY = 1040    # kg
AMBULANCE_EMISSIONS_PER_KM = 322            # grams of CO2 / km
AMBULANCE_CONSUMPTION_PER_KM = 0.122        # l / km
AMBULANCE_FUEL_CAPACITY = 90                # l
DIESEL_COST = 0.911                         # € / l
AMBULANCE_EMISSIONS_PER_LITER = 2.67        # kg of CO2 per liter of Diesel

# Conversions
HOURS_TO_MIN = 60

# Distribution centre
DIST_CENTER_LONG = -0.27787343210717297
DIST_CENTER_LAT = 36.07028912825954

# Blood demand parameters
BLOOD_AMOUNT_MEAN_NORMAL = 1.0              # blood units
BLOOD_AMOUNT_SIGMA_NORMAL = 1.4
BLOOD_AMOUNT_MIN_NORMAL = 0
BLOOD_AMOUNT_MAX_NORMAL = 5

BLOOD_INTERVAL_MEAN_NORMAL = 62.71          # minutes
BLOOD_INTERVAL_SIGMA_NORMAL = 20.61
BLOOD_INTERVAL_MIN_NORMAL = 20
BLOOD_INTERVAL_MAX_NORMAL = 100

BLOOD_AMOUNT_MEAN_CATASTROPHE = 2.8         # blood units
BLOOD_AMOUNT_SIGMA_CATASTROPHE = 2.95
BLOOD_AMOUNT_MIN_CATASTROPHE = 0
BLOOD_AMOUNT_MAX_CATASTROPHE = 11

# Simulation parameters
TIMESTEPS = 20*60                           # minutes

