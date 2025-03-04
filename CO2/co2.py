import csv
import matplotlib.pyplot as plt

x = [] # co2 %
y = [] # laiks

csvfname = "Aranet_2023-10-19.csv"
data = [] # dicts with DATE, CO2, TEMP, HUM%, P ATM

with open(csvfname, "r") as file:
    csvfile = csv.DictReader(file)
    
    for row in csvfile:
        x.append(row["Atmospheric pressure(mmHg)"])
        date, time = row["Time(dd/mm/yyyy)"].split()
        y.append(time)
        
fig, ax = plt.subplot()

ax.bar(x, y)
        
    
        
    
       
    
    