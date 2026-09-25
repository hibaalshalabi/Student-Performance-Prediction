import numpy as np
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'data.csv')

data = np.genfromtxt(file_path, delimiter=',', skip_header=1, usecols=range(0, 7))

print("Shape:", data.shape)
print("\nFirst 5 rows:\n", data[:5])
print("\nMissing values count:", np.isnan(data).sum())

print("Mean:", np.nanmean(data, axis=0))
print("Std:", np.nanstd(data, axis=0))
print("Min:", np.nanmin(data, axis=0))
print("Max:", np.nanmax(data, axis=0))
