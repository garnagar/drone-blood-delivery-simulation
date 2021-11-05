from distr_center import DistrCenter
from hospital import Hospital
from vehicles.drone import Drone
from vehicles.ambulance import Ambulance

def main():
    print("drone-blood-delivery-sim running")

    dst_test_1 = DistrCenter(0, -1.3042120313089076, 36.806186441462806)
    dst_test_2 = DistrCenter(1, -4.06218700915241, 39.6776812700527)
    hospital_1 = Hospital(0, -4.06218700915241, 39.6776812700527)
    hospital_2 = Hospital(1, -1.3042120313089076, 36.806186441462806)
    
    amb_1 = Ambulance(0, dst_test_1)
    drone_1 = Drone(0, dst_test_1)

    print(drone_1.isAvailable)
    

if __name__ == '__main__':
    main()
    
def dst_centers_setup(self):
    # parse locations.txt
    pass
