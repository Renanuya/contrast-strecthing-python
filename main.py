import numpy as np
import pandas as pd

data = pd.read_excel('data/example_data.xlsx')

dataAsNumpy = data.to_numpy()

L = 256
min_pixel_value = np.min(dataAsNumpy)
max_pixel_value = np.max(dataAsNumpy)

contrast_stretched_data = np.zeros_like(dataAsNumpy, dtype=np.float32)

for i in range(dataAsNumpy.shape[0]):
    for j in range(dataAsNumpy.shape[1]):
        contrast_stretched_data[i, j] = ((dataAsNumpy[i, j] - min_pixel_value) / (max_pixel_value - min_pixel_value)) * (L - 1)

new_contrast_stretched_data = contrast_stretched_data.astype(np.uint8)
new_contrast_stretched_data_as_data_frame = pd.DataFrame(new_contrast_stretched_data)

output_file_path = 'data/contrast_stretched_example_data.xlsx'
new_contrast_stretched_data_as_data_frame.to_excel(output_file_path, index=False, header=False)
print(new_contrast_stretched_data)
print("------------------------------------------------------------------")
print("Contrast stretched data has been saved to: ", output_file_path)
