import os
import nibabel as nib
import numpy as np


input_dir = 'Gauss_smooth'
output_dir = 'grey_normalized'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for filename in os.listdir(input_dir):
    if filename.endswith('.nii.gz'):
        img = nib.load(os.path.join(input_dir, filename))
        data = img.get_fdata()
        data_normalized = (data - np.min(data)) / (np.max(data) - np.min(data))
        img_normalized = nib.Nifti1Image(data_normalized, img.affine)
        nib.save(img_normalized, os.path.join(output_dir, filename))

