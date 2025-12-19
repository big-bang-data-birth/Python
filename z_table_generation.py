###########################################
#Reference: https://math.stackexchange.com/questions/1665823/how-to-manually-create-a-z-table
###########################################

from scipy.integrate import quad
import numpy as np
import pandas as pd

def normalProbabilityDensity(x):
    constant = 1.0 / np.sqrt(2*np.pi)
    return(constant * np.exp((-x**2) / 2.0) )


data={"index":[],"columns":[]}
index = np.round(np.arange(0, 4.1, .1),2)
columns = np.round(np.arange(0.00, .1, .01), 2)

standard_normal_table = pd.DataFrame(data, index, columns)

for index in standard_normal_table.index:
    for column in standard_normal_table.columns:
        z = np.round(index + column, 2)
        # Following comments for the quad library function used...
        # normalProbabilityDensity formula => https://www.itl.nist.gov/div898/handbook/eda/section3/eda3661.htm
        # library: https://docs.scipy.org/doc/scipy/tutorial/integrate.html
        # https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html
        value, _ = quad(normalProbabilityDensity, np.NINF, z)	# Simply integrate using the normalProbabilityDensity function in the given limits.	
        #value=normalProbabilityDensity(z)			#WRONG, SINCE NOT INTEGRATING FROM -INF TO Z value
        standard_normal_table.loc[index, column] = value

# Formatting to make the table look like a z-table 
standard_normal_table.index = standard_normal_table.index.astype(str)
standard_normal_table.columns = [str(column).ljust(4,'0') for column in standard_normal_table.columns]