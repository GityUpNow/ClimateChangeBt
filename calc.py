from time import *

start_time = 1483225200

start=1.0625;
increase= 0.0199;

def temperature():
    current = start + increase * ( (time() - start_time)/(24*3600*365))
    print "Calculated temperature..."
    return current
