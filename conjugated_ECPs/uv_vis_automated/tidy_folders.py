import json
import os

import os
import shutil

# Path to the main directory
main_directory = "C:/Users/kvriz/Desktop/Polymer_electronics_multimodal_database/conjugated_ECPs/uv_vis_automated"

# Loop through all folders in the main directory
for folder_name in os.listdir(main_directory):
    folder_path = os.path.join(main_directory, folder_name)
    
    # Check if it's a folder
    if os.path.isdir(folder_path):
        
        # Create a subfolder inside each folder
        subfolder_path = os.path.join(folder_path, 'molecular_structure')
        os.makedirs(subfolder_path, exist_ok=True)
        
        # Loop through all files in the folder
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            
            # Check if the file is a PNG image
            if file_name.lower().endswith('.png'):
                
                # Construct the path to move the PNG image into the 'abs_spectra' subfolder
                dest_path = os.path.join(subfolder_path, file_name)
                
                # Move the PNG image
                shutil.move(file_path, dest_path)
                print(f"Moved {file_path} to {dest_path}")
