# import required modules
import os
import numpy as np
import matplotlib.pyplot as plt

# assign directory to run throug
directory = "PÜ2/input_data"
 
# iterate over files in directory
for filename in os.listdir(directory):
    
    # checking if it is a power data file
    if filename.startswith("power_data") and filename.endswith(".txt"):
        
        # open file and convert to numpy array
        power_data_watts = open(os.path.join(directory, filename)).read().split("\n")
        data = np.array(power_data_watts)

        # get number of power data for plot
        number = filename.split("_")
        number = number[2].split(".")

        # plot data with multiple windows
        plt.figure("Power Data " + number[0])
        plt.title("Power Data " + number[0])
        plt.plot(data, color="red")

plt.show()