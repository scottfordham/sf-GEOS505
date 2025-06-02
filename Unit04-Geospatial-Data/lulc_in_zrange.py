import numpy as np


def lulc_in_zrange(zgrid, lulcgrid, zmin, zmax, lulckeys):
    
    
    # Get the land cover grid within the input elevation range
    
    # Get the histogram
    
    nbins = np.ones((zmin,zmax))
    lulcfrac = 1.0/4.0
    
    return nbins, lulcfrac