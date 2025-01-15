# Monthly Rainfall Distribution
# This project visualizes the monthly rainfall distribution for a specific region using a bar chart. It uses Python's matplotlib library to create a visually appealing representation of the data.

import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

rainfall = [75, 60, 100, 125, 175, 200, 225, 210, 180, 140, 90, 80]

#Plotting
plt.figure(figsize=(10,6))
plt.bar(months, rainfall, color = "skyblue", edgecolor="black")

plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.title('Monthly Rainfall Distribution', fontsize = 12)

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
