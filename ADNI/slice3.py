import os
import nibabel as nib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the meta data
meta_data = pd.read_csv('meta.csv')

# Create directories for the slices
os.makedirs('slice/x', exist_ok=True)
os.makedirs('slice/y', exist_ok=True)
os.makedirs('slice/z', exist_ok=True)

# Iterate over the files in the grey_normalized directory
for file in os.listdir('grey_normalized'):
    # Load the .nii.gz file
    img = nib.load(os.path.join('grey_normalized', file))
    data = img.get_fdata()

    # Extract the slices
    slice_x = data[90, :, :]
    slice_y = data[:, 108, :]
    slice_z = data[:, :, 90]

    # Get the subject ID from the file name
    subject_id = file.split('.')[0]

    # Get the group for this subject
    group = meta_data.loc[meta_data['Subject'] == subject_id, 'Group'].values[0]

    # Create directories for this group if they don't exist
    os.makedirs(os.path.join('slice/x', group), exist_ok=True)
    os.makedirs(os.path.join('slice/y', group), exist_ok=True)
    os.makedirs(os.path.join('slice/z', group), exist_ok=True)

    # Save the slices
    plt.imsave(os.path.join('slice/x', group, f'{subject_id}.png'), slice_x, cmap='gray')
    plt.imsave(os.path.join('slice/y', group, f'{subject_id}.png'), slice_y, cmap='gray')
    plt.imsave(os.path.join('slice/z', group, f'{subject_id}.png'), slice_z, cmap='gray')

print("All slices have been successfully saved in the corresponding directories.")

