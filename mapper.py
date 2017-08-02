#!/home/hadoop/anaconda/bin/python
import sys
import os
import os.path
import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt
import netCDF4
import numpy as np
import gc
import random
from mpl_toolkits.basemap import Basemap
from datetime import date, timedelta
import urllib

plt.ioff()
# open a local NetCDF file or remote OPeNDAP URL
try:
    for line in sys.stdin.readlines():
        sys.stderr.write('reporter:status:' + line)
        filename, headers = urllib.urlretrieve(line)
        nc = netCDF4.Dataset(filename)
        tasmax = nc.variables['tasmax']
        day = timedelta(days=tasmax.time) + date(2006,1,1)
        tasmax = tasmax[:]

        print day, tasmax.max(), tasmax.min(), tasmax.mean()
        gc.collect()
        os.remove(filename)
except:
    raise
finally:
    try:
        os.remove(filename)
    except:
        pass
