import matplotlib.pyplot as plt
import datetime

# Data to plot
dates = [datetime.datetime(2022, 1, 1), datetime.datetime(2022, 1, 2),
         datetime.datetime(2022, 1, 3), datetime.datetime(2022, 1, 4)]
values = [5, 10, 15, 20]

# Create the figure and a subplot
fig, ax = plt.subplots()

# Plot the data as a line chart
ax.plot(dates, values)

# Format the x-axis as dates
fig.autofmt_xdate()

# Show the plot
plt.show()