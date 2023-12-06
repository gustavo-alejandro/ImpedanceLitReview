# import necessary libraries
import pandas as pd
import os
import glob
import matplotlib.pyplot as plt

# use glob to get all the csv files
# in the folder
path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "*.xlsx"))

df = pd.read_excel(csv_files[0])
# Plot all pairs of columns in the same scatter plot
plt.figure(figsize=(12, 7))
#plt.figure()
# Iterate through pairs of columns
for i in range(0, df.shape[1], 2):
    x_col = df.columns[i]
    y_col = df.columns[i + 1]
    plt.scatter(df[x_col], df[y_col], label=f'{y_col}', s=3)

plt.xlabel('Zr [ohm]')
plt.ylabel('-Zim [ohm]')
plt.title('Impedance measurement in Hall-Heroult cells Lit. review')
plt.grid(True)
plt.legend()
ax = plt.gca()
ax.set_aspect('equal', adjustable='box')

plt.show()