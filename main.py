# coding=utf-8


from DistribCenter import DistrbCenter
from hospital import Hospital


def main():
    print("drone-blood-delivery-sim running")

    dst_test = DistrbCenter(0, -1.3042120313089076, 36.806186441462806)
    hospital = Hospital(0, -4.06218700915241, 39.6776812700527)

    dst_test.get_distance_hospital(hospital)
    



if __name__ == '__main__':
    main()
    
def dst_centers_setup(self):
    # parse locations.txt
    pass
