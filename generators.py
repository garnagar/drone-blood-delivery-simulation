import numpy as np
import scipy.stats as stats

def generate_boold_demand_tseries_normal(amount_mean, amount_sigma, amount_min, amount_max,
                                         t_mean, t_sigma, t_min, t_max, length):
    ts = np.zeros(length)

    # Create random distribution for blood amounts per surgery
    a = (amount_min - amount_mean) / amount_sigma
    b = (amount_max - amount_mean) / amount_sigma
    amount_dist = stats.truncnorm(a, b, loc = amount_mean, scale = amount_sigma)

    # Create random distribution for time intervals between surgeries
    a = (t_min - t_mean) / t_sigma
    b = (t_max - t_mean) / t_sigma
    t_dist = stats.truncnorm(a, b, loc=t_mean, scale=t_sigma)

    # Generate time series
    t = 0
    while True:
        t = t + t_dist.rvs(1).astype(int)
        if t < length:
            ts[t] = amount_dist.rvs(1).astype(int)
        else:  # Finish if length of series is exceeded
            break
    return ts