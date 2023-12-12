import rplidar
import time
from scipy.io import savemat
import numpy as np
import pandas as pd
import serial



def scan(lidar: rplidar.RPLidar):
    iterator = lidar.iter_scans()
    count = 0
    for i in iterator:
        if count == 1:
            print(i)
            return i
        count +=1


def main():

    Flag = True
    number_of_scans = 0
    lidar = None
    ydirs = [0]

    while Flag == True:
        
        choice = str(input("Input: "))

        if choice == "Open": 
            lidar = rplidar.RPLidar("COM7")         
            lidar.reset()                           
            arduino = serial.Serial("COM10",9600)    
            time.sleep(5)
            Data = scan(lidar)
            Data = pd.DataFrame(Data).to_csv(f'Scan_{number_of_scans}.csv')
            number_of_scans = number_of_scans + 1


        if choice == "Scan":
            arduino.write("S".encode('utf-8'))
            print("Sent 'S', now sleeping for 10 seconds")
            time.sleep(10)
            Data = scan(lidar)
            Data = pd.DataFrame(Data).to_csv(f'Scan_{number_of_scans}.csv')
            number_of_scans +=1
            ydir = int(arduino.read_all())
            ydirs.append(ydir)


if __name__ == "__main__":
    main()
