import fastf1 as ff1
import fastf1.plotting
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd  

try:
    year = int(input("What year would you like to see qualifying from?: "))
except:
    print("That is not a valid year")

try:
    race = int(input("What round would you like to see qualifying comparison from?: "))
except:
    print("That is not a valid round")

session = ff1.get_session(year, race, 'Q')
session.load()

drivers = pd.unique(session.laps['Driver'])

fl = {}
delta = list()
colors = list()

print(drivers)
fastest = session.laps.pick_fastest()['LapTime']

for driver in drivers:
    try:
        delta_to_1 = session.laps.pick_drivers(driver).pick_fastest()['LapTime'] - fastest
        delta.append(delta_to_1.seconds + delta_to_1.microseconds / 1000000)
        fl[driver] = delta_to_1
        colors.append(ff1.plotting.get_driver_color(session=session, identifier=driver))
    except:
        drivers = np.delete(drivers, np.where(drivers == driver))

print(colors)
plt.style.use('grayscale')
plt.gca().invert_yaxis()
plt.gca().set_facecolor('#A6A09F')

plt.barh(drivers, delta, color=colors)
plt.ylabel("Drivers")
plt.xlabel('Time Delta')
plt.show()