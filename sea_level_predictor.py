import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    fig, ax = plt.subplots()
    plt.scatter(x, y)

    # Create first line of best fit
    regress = linregress(x, y)
    x_predict = pd.Series([i for i in range(1880, 2051)])
    y_predict = regress.slope * x_predict + regress.intercept

    plt.plot(x_predict, y_predict, 'blue')

    # Create second line of best fit
    df2 = df.loc[df['Year'] >= 2000]
    x2 = df2['Year']
    y2 = df2['CSIRO Adjusted Sea Level']

    regress2 = linregress(x2, y2)
    x2_predict = pd.Series([i for i in range(2000, 2051)])
    y2_predict = regress2.slope * x2_predict + regress2.intercept
    
    plt.plot(x2_predict, y2_predict, 'red')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()