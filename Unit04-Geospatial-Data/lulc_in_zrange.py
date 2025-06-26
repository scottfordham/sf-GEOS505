import numpy as np

def z_in_range(z_array, zmin, zmax):
    
    # 1. Create a masked array that is identical to z_array in dimensions,
    #    but where values outside zmin to zmax are masked
    z_ma = np.ma.masked_outside(z_array, zmin, zmax)
        
    # 2. Return the masked array
    return z_ma

def lulc_in_zrange(lulc_array, lulc_bins, z_array, zmin, zmax):
    
    # 1. Get the masked array with the elevation range input by the user by calling
    #    the function above
    z_ma = z_in_range(z_array, zmin, zmax)
    
    # 2. Get the LULC values within the elevation range mask given in z_ma
    lulc_ma = np.ma.masked_array(lulc_array, ~z_ma.mask)
    
    # 3. Get the histogram of LULC in lulc_ma
    lulc_1d = lulc_ma.data[lulc_ma.mask] # 1D vector of LULC not masked
    
    lulc_counts = np.zeros(lulc_bins.size)
    
    for i in np.arange(lulc_bins.size):
        lulc_counts[i] = np.count_nonzero(lulc_1d == lulc_bins[i])
    
    # 4. Return LULC histogram
    return lulc_counts