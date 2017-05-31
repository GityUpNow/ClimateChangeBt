from time import *

start_time = 1483138800

start=1.0876;
increase= 0.0199;

def temperature():
    current = start + increase * ( (time() - start_time)/(24*3600*365))
    print "Calculated temperature..."
    return current
