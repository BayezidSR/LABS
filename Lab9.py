import numpy as np

def read_values_from_file(filename):
    values = np.loadtxt(filename)
    return values

data = read_values_from_file("values.txt")
print(data)

#----------------------------------------------------------------------------------------------------------------

def read_oscillatory_wave_data(filename):
    data = np.loadtxt(filename, delimiter=',')
    
    amplitudes = data[:, 1]
    
    mean_amplitude = np.mean(amplitudes)
    max_amplitude = np.max(amplitudes)
    
    return mean_amplitude, max_amplitude

mean_amp, max_amp = read_oscillatory_wave_data("wave_data.csv")
print("Mean amplitude:", mean_amp)
print("Max amplitude:", max_amp)

#----------------------------------------------------------------------------------------------------------------

def read_standing_wave_data(filename):
    data = np.loadtxt(filename, delimiter=',')
    
    tensions = data[:, 1]
    mu = 1
    wave_speeds = np.sqrt(tensions / mu)
    
    return wave_speeds

speeds = read_standing_wave_data("standing_wave.csv")
print("Wave speeds:", speeds)

#----------------------------------------------------------------------------------------------------------------

