
import matplotlib.pyplot as plt
import numpy as np


def plot_curve(x_values, y_values):
    print(f"Your x values: {x_values}")
    print(f"Your y values: {y_values}")
    plt.plot(x_values, y_values)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Curve Plot')
    plt.show()
    return 

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])
plot_curve(x,y)

#---------------------------------------------------------------------------------

def plot_hr_diagram(temperature, luminosity):

    plt.scatter(temperature, luminosity, c=temperature, cmap='plasma', edgecolors='k')
    plt.gca().invert_xaxis()
    plt.xlabel("Temperature")
    plt.ylabel("Luminosity")
    plt.title("Hertzsprung-Russell Diagram")
    plt.colorbar(label="Temperature")
    plt.show()
    return 

temperature = np.array([5000, 6000, 7000, 8000])
luminosity = np.array([1.0, 1.5, 2.0, 2.5])
plot_hr_diagram(temperature, luminosity)

#------------------------------------------------------------------------------------------- 

def plot_density(data, color_map='gray'):
    
    plt.hist2d(data[:, 0], data[:, 1], bins=50, cmap=color_map, density=True)
    plt.colorbar(label="Density")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.title("Density Plot")
    plt.show()
    return 
np.random.seed(0)
data = np.random.randn(1000, 2)
plot_density(data, 'hot')