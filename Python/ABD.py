import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import Point
import random

def load_scan(scanname: str):
    scan_0 = pd.read_csv(f'{scanname}',names=['Index','Quality','Theta','Distance'], header=0)
    scan_0 = scan_0.assign(Radians = lambda x: x['Theta'].apply(lambda y: math.radians(y)))
    scan_0 = scan_0.assign(X = lambda x: (x['Radians']).apply(lambda y: math.sin(y)),
                           Y = lambda x: (x['Radians']).apply(lambda y: math.cos(y)))
    scan_0 = scan_0.assign(X = lambda x: (x['Distance']*x['X']),
                           Y = lambda x: (x['Distance']*x['Y']))
    return scan_0



def Dmax(point_curr: Point.Point, point_prev: Point.Point):
    return random.random() > 0.5
    


def ABD(data: pd.DataFrame):
    breakpoint_list = []
    for prev_row, curr_row in zip(data.index, data.index[1:]):
        point_prev = Point.Point(data.iloc[curr_row])
        point_curr = Point.Point(data.iloc[prev_row])
        isbreakpoint = Dmax(point_curr, point_prev)
        if isbreakpoint == True:
            breakpoint_list.append(point_curr.index)
    return breakpoint_list



def main():
    data = load_scan("Scan_0.csv")
    breakpoint_list = ABD(data)
    print(breakpoint_list)
    

main()
