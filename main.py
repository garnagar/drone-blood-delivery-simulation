# coding=utf-8


from DistribCenter import DistrbCenter
from hospital import Hospital


def main():
    print("drone-blood-delivery-sim running")

    dst_test_1 = DistrbCenter(0, -1.3042120313089076, 36.806186441462806)
    hospital_1 = Hospital(0, -4.06218700915241, 39.6776812700527)
    hospital_2 = Hospital(0, -1.3042120313089076, 36.806186441462806)
    dst_test_2 = DistrbCenter(1, -4.06218700915241, 39.6776812700527)

    dst_test_1.get_distance_hospital(hospital_1)
    dst_test_2.get_distance_hospital(hospital_2)
    

if __name__ == '__main__':
    main()
    
def dst_centers_setup(self):
    # parse locations.txt
    pass
